# @author: main
# @file: 2023/4/17
# time: 2023-04-17 15:57
import hashlib
import json
import random
import re
import time

import execjs
import requests

from api.极验.jiyan_cryptio import Rsa, Cbc
from huanjing import get_huanjing


def get_token():
    t = hashlib.md5((generate_random_string(32) + str(int(time.time()))).encode()).hexdigest()
    return t


def generate_random_string(length):
    char_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    rand_string = ""
    for i in range(length):
        rand_string += random.choice(char_list)
    return rand_string


# 深知V2的主函数
class Jiyan_Shenzhi_v2():
    def __init__(self, id="449727cc395032a34f71d9b7b13cb02e"):
        self.key = ''.join([random.choice('0123456789abcdef') for _ in range(16)])
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
        self.session = requests.session()
        self.session.headers = headers
        self.id = id

    def get_v2_sense(self):
        params = {
            "callback": "geetest_{}".format(str(int(time.time() * 1000))),
        }
        url = 'https://dkapi.geetest.com/deepknow/v2/gettype'
        v2_sense = self.session.get(url, params=params)
        load_info = json.loads(v2_sense.text.replace(f'{params["callback"]}(', '')[:-1])
        self.gct = load_info['gct_path']

    def get_jct4(self):
        jct4_url = 'https://static.geetest.com' + self.gct
        jct4_resp = self.session.get(jct4_url)
        jct4_js = jct4_resp.content.decode()
        fangfa = re.findall(r"t\[e\]=(.*?)(?:\[|\()", jct4_js)[0]
        end_jct4 = jct4_js.replace(f"return function(t)",
                                   f";this.daochu = {fangfa};this.daochu_e = e;return function(t)")
        jact4_run = execjs.compile(end_jct4)
        key = jact4_run.eval("this.daochu_e")
        value = jact4_run.call("this.daochu", "")
        self.keys = key
        self.values = value

    def get_h(self):
        rsa = Rsa()
        self.h = rsa.Rencrypt(self.key)  # 这个就是u

    def get_e(self):
        NFeB = {
            "id": self.id,
            "page_id": int(time.time() * 1000),
            "lang": "zh-cn",
            self.keys: self.values,
            "data": {
                "insights": get_huanjing(),
                "track_key": 0,
                "track": [],
                "ep": {
                    "ts": int(time.time() * 1000),
                    "v": "2.3.0",
                    "f": "406ec650",
                    "em": {
                        "ph": 0,
                        "cp": 0,
                        "ek": "11",
                        "wd": 1,
                        "nt": 0,
                        "si": 0,
                        "sc": 0
                    },
                    "te": False,
                    "me": False,
                    "do": False,
                    "ot": -1,
                    "tm": {
                        "a": int(time.time() * 1000),
                        "b": int(time.time() * 1000),
                        "c": int(time.time() * 1000),
                        "d": 0,
                        "e": 0,
                        "f": int(time.time() * 1000),
                        "g": int(time.time() * 1000),
                        "h": int(time.time() * 1000),
                        "i": int(time.time() * 1000),
                        "j": int(time.time() * 1000),
                        "k": int(time.time() * 1000),
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
                    },
                    "action": "client",
                    "iip": ""
                },
                "eco": get_token(),
                "ww3": ""
            }
        }
        return json.dumps(NFeB, indent=None, separators=(',', ':'))

    def get_l(self):
        cbc = Cbc(self.key, '0000000000000000')
        self.l = cbc.Shenzhi_v2(self.get_e())

    # 初始化模块
    def init(self):
        self.get_v2_sense()
        self.get_jct4()
        self.get_h()
        self.get_l()
        self.verify()

    def verify(self):
        verify_url = 'https://dkapi.geetest.com/deepknow/v2/judge?pt=1&app_id={}'.format(self.id)
        data = self.l+self.h
        verify_req = self.session.post(verify_url,data=data)
        print(verify_req.json())
if __name__ == '__main__':
    jiyan = Jiyan_Shenzhi_v2()
    jiyan.init()
