# @author: 极验三代点选
# @file: 2023/4/13
# time: 2023-04-13 16:02
import json
import random
import time

import requests


def get_random():
    def t():
        random_num = random.randint(1, 65536)
        random_str = hex(random_num)[2:].zfill(4)
        return random_str

    return t() + t() + t() + t()


class JiYan_v3:
    def __init__(self, captcha_id):
        self.type = 'click'
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Sec-Fetch-Dest': 'script',
            'Sec-Fetch-Mode': 'no-cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        self.session = requests.session()
        self.session.verify = False
        # self.session.proxies = {"https": "http://127.0.0.1:10809"}
        self.session.headers = headers
        self.captchaId = captcha_id
        self.gt = 'ce33de396f8d04030f6eca8fbd225070'
        self.challenge = captcha_id

    def timeC(self):
        t = int(time.time() * 1000)
        return str(t)

    def get_load_2(self):
        url = 'https://api.geevisit.com/get.php'
        params = {
            'is_next': "true",
            'gt': self.gt,
            'challenge': self.challenge,
            'type': 'click',
            'lang': 'zh',
            'https': 'false',
            'protocol': 'https://',
            'offline': 'false',
            'product': 'popup',
            'api_server': 'api.geevisit.com',
            'isPC': 'true',
            'autoReset': 'true',
            'showBack': 'true',
            'width': '100%',
            'callback': 'geetest_' + self.timeC()
        }
        resp = self.session.get(url, params=params)
        load_info = resp.text.replace(f'{params["callback"]}(', '')[:-1]
        return json.loads(load_info)

    def get_load_1(self):
        params = {
            'gt': self.gt,
            'challenge': self.challenge,
            'lang': 'zh-cn',
            'pt': '0',
            'client_type': 'web',
            'w': "",
            'callback': 'geetest_' + self.timeC()}

        response = self.session.get('https://api.geetest.com/get.php', params=params)
        load_info = response.text.replace(f'{params["callback"]}(', '')[:-1]
        return json.loads(load_info)


if __name__ == '__main__':
    v3 = JiYan_v3("baaff60ce2e88f7c1c83582bb52043b2")
    print(v3.get_load_2())
