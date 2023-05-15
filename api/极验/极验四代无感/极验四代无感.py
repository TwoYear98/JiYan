import hashlib
import json
import random
import re
import time
import uuid
from datetime import datetime

import execjs
import pytz
import requests

from api.极验.jiyan_cryptio import Rsa, Cbc

def get_uuid(lens=32):
    return str(uuid.UUID(''.join([random.choice('0123456789abcdef') for _ in range(lens)])))


def md5s(string):
    md5 = hashlib.md5()

    # 更新对象内容，以字符串进行编码
    md5.update(string.encode('utf-8'))

    # 获取加密后的十六进制字符串
    result = md5.hexdigest()
    return str(result)


def get_time_geshi():
    tz = pytz.timezone('Asia/Shanghai')  # 设置时区为中国标准时间
    dt = datetime.now(tz)
    timestamp = dt.isoformat()

    return str(timestamp)


def get_random():
    def t():
        random_num = random.randint(1, 65536)
        random_str = hex(random_num)[2:].zfill(4)
        return random_str

    return t() + t() + t() + t()


class JiYan:
    def __init__(self, captchaId='24f56dc13c40dc4a02fd0318567caef5'):
        self.uid = get_uuid()
        self.type = 'ai'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        self.session = requests.session()
        self.session.headers = headers
        self.captchaId = captchaId
        self.gt = ''

    def timeC(self):
        t = int(time.time() * 1000)
        return str(t)

    def get_demo(self):
        url = 'https://www.geetest.com/adaptive-captcha-demo'
        resp = self.session.get(url)
        demo_js = re.findall('href="(/_next/static.*?adaptive-captcha-demo\\.js)"', resp.text)[0]
        return 'https://www.geetest.com' + demo_js

    def get_captchaId(self, demo_url):
        resp = self.session.get(demo_url)
        self.captchaId = re.findall('captchaId:"(.*?)"', resp.text)[0]

    def get_load(self):
        url = 'https://gcaptcha4.geetest.com/load'
        params = {
            'captcha_id': self.captchaId,
            'challenge': self.uid,
            'client_type': 'web',
            'risk_type': self.type,
            'lang': 'zh',
            'callback': 'geetest_' + self.timeC()
        }
        resp = self.session.get(url, params=params)
        load_info = resp.text.replace(f'{params["callback"]}(', '')[:-1]
        return json.loads(load_info)

    def info_analysis(self, load_info):
        # ques = load_info['data']['ques']
        lot_number = load_info['data']['lot_number']
        datetime = load_info['data']['pow_detail']['datetime']
        payload = load_info['data']['payload']
        process_token = load_info['data']['process_token']
        return {
            'lot_number': lot_number,
            'payload': payload,
            'process_token': process_token,
            # 'end_ques': juzhen_suanfa(ques),
            'datetime': datetime
        }

    def get_jct4(self, path):
        jct4_url = 'https://static.geetest.com' + path
        jct4_resp = self.session.get(jct4_url)
        jct4_js = jct4_resp.content.decode()
        fangfa = re.findall(r"t\[e\]=(.*?)(?:\[|\()", jct4_js)[0]
        end_jct4 = jct4_js.replace(f"return function(t)",
                                   f";this.daochu = {fangfa};this.daochu_e = e;return function(t)")
        jact4_run = execjs.compile(end_jct4)
        key = jact4_run.eval("this.daochu_e")
        value = jact4_run.call("this.daochu", "")
        return str(key), str(value)

    def structure(self, info, key, value):
        # userresponse = info["end_ques"]
        _ = f"1|0|md5|{info.get('datetime')}|{self.captchaId}|{info.get('lot_number')}||"
        h = get_random()
        pow_msg = _ + str(h)
        pow_sign = md5s(pow_msg)
        e = {
            "device_id": "2d8aefc681fd34980a026cfbf46e7277",
            "em": {
                "ph": 0,
                "cp": 0,
                "ek": "11",
                "wd": 1,
                "nt": 0,
                "si": 0,
                "sc": 0
            },
            "ep": "123",
            "geetest": "captcha",
            "lang": "zh",
            "lot_number": info['lot_number'],
            "passtime": 345,
            "pow_msg": pow_msg,
            "pow_sign": pow_sign,
            key: value,
            # "userresponse": userresponse,
        }
        return e

    def genKey(self):
        t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        n = ''
        for i in range(16):
            n += random.choice(t)
        return n

    def encry(self, e, key):
        rsa = Rsa()
        u = rsa.Rencrypt(key)  # 这个就是u
        cbc = Cbc(key, '0000000000000000')
        c = cbc.encrypt(json.dumps(e))
        return str(c) + str(u)

    def verify(self, w, info):
        url = 'http://gcaptcha4.geetest.com/verify'
        params = {
            'callback': 'geetest_' + self.timeC(),
            'captcha_id': self.captchaId,
            'client_type': 'web',
            'lot_number': info['lot_number'],
            'risk_type': self.type,
            'payload': info['payload'],
            'process_token': info['process_token'],
            'payload_protocol': 1,
            'pt': 1,
            'w': w
        }
        resp = self.session.get(url, params=params)
        result = json.loads(resp.text[22:-1])
        print(result)
        if result.get("data").get("result") == "success":
            return 1
        return {}

    def run(self):
        load_info = self.get_load()
        jct4_path = load_info['data']['gct_path']
        key, value = self.get_jct4(jct4_path)
        info = self.info_analysis(load_info)
        e = self.structure(info, key, value)
        key = ''.join([random.choice('0123456789abcdef') for _ in range(16)])
        w = self.encry(e, key)
        result = self.verify(w, info)
        return result


if __name__ == '__main__':
    jishu = 0
    for i in range(100):
        j = JiYan()
        result = j.run()
        if result == 1:
            jishu += 1

    print(f"请求了100次，成功率{jishu}%")
