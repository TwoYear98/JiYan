# @author: wugan
# @file: 2023/4/14
# time: 2023-04-14 15:59
import base64
import json
import random
import re
import time

import execjs
import requests

from api.极验.jiyan_cryptio import Cbc, Rsa
from huanjing import get_huanjing
from urllib.parse import urlencode

class Jiyan_v3_wugan():
    def __init__(self, gt, challenge):
        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        self.session.verify = False
        # self.session.proxies = {"https": "http://127.0.0.1:10809"}
        self.session.timeout = 10
        self.gt = gt
        self.challenge = challenge
        self.key = ''.join([random.choice('0123456789abcdef') for _ in range(16)])

    def chushihua(self):
        url = 'https://www.geetest.com/demo/gt/register-fullpage?t={}'.format(str(int(time.time() * 1000)))
        req = self.session.get(url)
        self.challenge = req.json().get("challenge")
        self.gt = req.json().get("gt")

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

    def timeC(self):
        t = int(time.time() * 1000)
        return str(t)

    def base64_api(self,img_url):
        res = self.session.get(img_url).content
        base64_data = base64.b64encode(res)
        b64 = base64_data.decode()
        data = {"username": "himyidea", "password": 'hmyd188', "typeid": 27, "image": b64}
        result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
        if result['success']:
            return result["data"]["result"]
        else:
            # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
            return result["message"]
        return ""

    def get_click_xy(self,img_url):
        content = (self.base64_api("https://static.geetest.com" + img_url))
        zuobiao = ''
        xys = content.split("|")
        for xy in xys:
            xy0 = xy.split(",")
            x = int(xy0[0])
            y = int(xy0[1])
            final_x = int(round(x / 333.375 * 100 * 100, 0))
            final_y = int(round(y / 333.375 * 100 * 100, 0))
            zuobiao = zuobiao + str(final_x) + "_" + str(final_y) + ","
        zuobiao = zuobiao[:-1]
        return zuobiao

    def get_req_w(self):
        '''
        三代统一的W，每次请求使用这个获取
        :return:
        '''
        Config = {
            "gt": self.gt,
            "challenge": self.challenge,
            "lang": "zh-cn",
            "offline": False,
            "new_captcha": True,
            "width": "100%",
            "product": "popup",
            "protocol": "https://",
            "type": "fullpage",
            "static_servers": [
                "static.geetest.com/",
                "dn-staticdown.qbox.me/"
            ],
            "beeline": "/static/js/beeline.1.0.1.js",
            "voice": "/static/js/voice.1.2.2.js",
            "click": "/static/js/click.3.0.8.js",
            "fullpage": "/static/js/fullpage.9.1.4.js",
            "slide": "/static/js/slide.7.9.0.js",
            "geetest": "/static/js/geetest.6.0.9.js",
            "aspect_radio": {
                "slide": 103,
                "click": 128,
                "voice": 128,
                "beeline": 50
            },
            "cc": 8,
            "ww": True,
            "i": get_huanjing()
        }
        cbcc = Cbc(self.key, '0000000000000000')
        rsa = Rsa()
        u = rsa.Rencrypt(self.key)  # 这个就是u
        w = str(cbcc.v3_ncrypt(json.dumps(Config, indent=None, separators=(',', ':')))) + str(u)
        return w

    def create_web_task(self):
        '''
        无感的加载，获取信息
        :return:
        '''
        params = {
            'gt': self.gt,
            'challenge': self.challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'client_type': 'web',
            'w': self.get_req_w(),
            'callback': 'geetest_' + self.timeC(),
        }

        response = self.session.get('https://api.geevisit.com/get.php', params=params)
        load_info = response.text.replace(f'{params["callback"]}(', '')[:-1]
        return json.loads(load_info)

    def verify_web(self):
        '''
        无感的提交，返回的是一个jsonf
        :return:
        '''
        params = {
            'gt': self.gt,
            'challenge': self.challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'client_type': 'web',
            'w': self.get_web_two_w(),
            'callback': 'geetest_' + self.timeC(),
        }
        print(json.dumps(params))
        response = self.session.get('https://api.geevisit.com/ajax.php', params=params)
        load_info = response.text.replace(f'{params["callback"]}(', '')[:-1]
        return json.loads(load_info)

    def get_web_two_w(self):
        '''
        无感的第二个w
        :return:
        '''
        t1 = int(time.time() * 1000)
        two_w_dict = {"lang": "zh-cn",
                      "type": "fullpage",
                      "tt": None,
                      "light": "SPAN_0",
                      "s": "",
                      "h": "",
                      "hh": "",
                      "hi": "",
                      "vip_order": -1,
                      "ct": -1,
                      "ep": {"v": "9.1.4", "te": False, "$_BBy": True, "ven": "Google Inc. (Google)",
                             "ren": "ANGLE (Google, Vulkan 1.3.0 (SwiftShader Device (Subzero) (0x0000C0DE)), SwiftShader driver)",
                             "fp": ["move", random.randint(1300, 1400), random.randint(250, 300), t1 + 100,
                                    "pointermove"],
                             "lp": ["up", random.randint(900, 950), random.randint(100, 150),
                                    t1 + random.randint(100, 150), "pointerup"],
                             "em": {"ph": 0, "cp": 0, "ek": "11", "wd": 1, "nt": 0, "si": 0, "sc": 0},
                             "tm": {"a": int(time.time() * 1000), "b": int(time.time() * 1000),
                                    "c": int(time.time() * 1000), "d": 0,
                                    "e": 0, "f": int(time.time() * 1000),
                                    "g": int(time.time() * 1000), "h": int(time.time() * 1000),
                                    "i": int(time.time() * 1000),
                                    "j": int(time.time() * 1000), "k": 0,
                                    "l": int(time.time() * 1000), "m": int(time.time() * 1000),
                                    "n": int(time.time() * 1000),
                                    "o": int(time.time() * 1000),
                                    "p": int(time.time() * 1000), "q": int(time.time() * 1000),
                                    "r": int(time.time() * 1000),
                                    "s": int(time.time() * 1000),
                                    "t": int(time.time() * 1000), "u": int(time.time() * 1000)}, "dnf": "dnf", "by": 0},
                      "passtime": random.randint(100, 300),
                      "rp": "", "captcha_token": "1777665468"}
        cbcc = Cbc(self.key, '0000000000000000')
        w = str(cbcc.v3_ncrypt(json.dumps(two_w_dict, indent=None, separators=(',', ':'))))
        return w

    def get_click_task(self):
        '''
        获取点击任务
        :return:
        '''
        params = {
            'gt': self.gt,
            'challenge': self.challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'client_type': 'web',
            'w': self.get_req_w(),
            'callback': 'geetest_' + self.timeC(),
        }
        response = self.session.get('https://api.geetest.com/get.php', params=params)
        print(response.text)
        load_info = json.loads(response.text.replace(f'{params["callback"]}(', '')[:-1])
        self.pic = load_info.get("data").get("pic")
        self.click_xy = self.get_click_xy(self.pic)
        jct4_path = load_info['data']['gct_path']
        self.keys, self.value = self.get_jct4(jct4_path)

        return load_info

    def get_verify_w(self):
        verify_w = {
            "lang": "zh-cn",
            "passtime": random.randint(800, 1000),
            "a": self.click_xy,
            "pic": self.pic,
            "tt": None,
            "ep": {
                "ca": None,
                "v": "3.0.8",
                "$_FI": False,
                "$_Jp": True,
                "tm": {
                    "a": int(time.time() * 1000),
                    "b": 0,
                    "c": 0,
                    "d": 0,
                    "e": 0,
                    "f": int(time.time() * 1000),
                    "g": int(time.time() * 1000),
                    "h": int(time.time() * 1000),
                    "i": int(time.time() * 1000),
                    "j": int(time.time() * 1000),
                    "k": 0,
                    "l": int(time.time() * 1000),
                    "m": int(time.time() * 1000),
                    "n": int(time.time() * 1000),
                    "o": int(time.time() * 1000),
                    "p": int(time.time() * 1000),
                    "q": int(time.time() * 1000),
                    "r": int(time.time() * 1000),
                    "s": int(time.time() * 1000),
                    "t": int(time.time() * 1000),
                    "u": int(time.time() * 1000)
                }
            },
            self.keys: self.value,
            "rp": None
        }
        print(f"等待加密的数据：{json.dumps(verify_w)}")

        rsa = Rsa()
        u = rsa.Rencrypt(self.key)  # 这个就是u

        cbcc = Cbc(self.key, '0000000000000000')
        w = str(cbcc.v3_ncrypt(json.dumps(verify_w, indent=None, separators=(',', ':'))))
        return str(w) + str(u)

    def verify_click(self):
        '''
        无感的提交，返回的是一个json
        :return:
        '''
        params = {
            'gt': self.gt,
            'challenge': self.challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'client_type': 'web',
            'w': self.get_verify_w(),
            'callback': 'geetest_' + self.timeC(),
        }
        url = 'https://api.geetest.com/ajax.php?' + urlencode(params)


        print(url)
        exit()
        response = self.session.get('https://api.geevisit.com/ajax.php', params=params)
        load_info = response.text.replace(f'{params["callback"]}(', '')[:-1]
        print(response.url)
        return json.loads(load_info)


    def run(self):
        print(self.create_web_task())
        print(self.verify_web())
        print(self.get_click_task())
        print(self.verify_click())

if __name__ == '__main__':
    v3 = Jiyan_v3_wugan("ce33de396f8d04030f6eca8fbd225070", "f7a227806c3bcccd56ac1a6bace314a4")
    # v3.chushihua()
    v3.run()
