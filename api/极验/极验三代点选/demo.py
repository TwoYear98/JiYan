import base64
import json
import re
import time

import requests
from bs4 import BeautifulSoup
# fullpage.9.1.4
from loguru import logger

from wugan import Jiyan_v3_wugan


def geet(data):
    # print(data)
    soup = BeautifulSoup(data, "lxml")
    results = soup.find_all(id='main-iframe')
    result = results[0]
    src = result['src']
    url = "https://makeabooking.flyscoot.com"
    session = requests.session()
    # session.cookies.update(cookie)
    try:
        url_ = url + src
        res = session.get(url_, verify=False)
        text = res.text
        logger.debug(text)
        if text.__contains__("This request was blocked by our security service"):
            logger.error("ip被封")
            return False
        swcngeec_ = text.find("SWCNGEEC=")
        swcngeec_ = swcngeec_ + len("SWCNGEEC=")
        text1 = text[swcngeec_:]
        end = text1.find('"')
        swcngeec = text1[0:end]

        dai = "".join(re.findall(r"&dai=(.*?)&", res.text))
        cts = "".join(re.findall(r"&cts=(.*?)", res.text))
        SWCGHOEL_ = text.find("SWCGHOEL=")
        text2 = text[SWCGHOEL_:]
        end = text2.find('"')
        swc = text2[0:end]
        s = int(time.time())
        t = int(time.time() * 1000)
        url_ = "https://makeabooking.flyscoot.com/_Incapsula_Resource?SWCNGEEC=" + swcngeec
        res = session.get(url_, verify=False)
        text = res.text
        # text = '{"challenge": "d61e003fda6ec1b92fb74a57bd69ba14", "gt": "ce33de396f8d04030f6eca8fbd225070", "new_captcha": true, "success": 1}'
        jstr = json.loads(text)
        challenge = jstr['challenge']
        gt = jstr['gt']
        v3 = Jiyan_v3_wugan(gt=gt, challenge=challenge)
        v3.run()
        print(gt)
        print(challenge)
        validate = input()
        params = (
            ('SWCGHOEL', 'gee'),
            ('dai', dai),
            ('cts', cts),
        )

        data = {
            'geetest_challenge': challenge,
            'geetest_validate': validate,
            'geetest_seccode': f'{validate}|jordan'
        }

        response = session.post('https://makeabooking.flyscoot.com/_Incapsula_Resource',
                                 params=params, data=data)
        print(response.text)
        print(response.status_code)
        print(response.cookies)
        print(response.headers)
        home_req = session.get('https://makeabooking.flyscoot.com/')
        print(home_req.text)
    finally:
        session.close()
    return True


def get_tp(img_path):
    result = base64_api(uname='himyidea', pwd='hmyd188', img=img_path, typeid=27)
    print(result)
    return result


# 一、图片文字类型(默认 3 数英混合)：
# 三、图片坐标点选类型：
# 19 :  1个坐标
# 20 :  3个坐标
# 21 :  3 ~ 5个坐标
# 22 :  5 ~ 8个坐标
# 27 :  1 ~ 4个坐标
# 48 : 轨迹类型

def base64_api(uname, pwd, img, typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        # ！！！！！！！注意：返回 人工不足等 错误情况 请加逻辑处理防止脚本卡死 继续重新 识别
        return result["message"]
    return ""


if __name__ == '__main__':
    data = '<html style="height:100%"><head><META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW"><meta name="format-detection" content="telephone=no"><meta name="viewport" content="initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><script src="/rtaliuery-Doct-The-Then-throngling-Was-Son-Hes-I" async></script></head><body style="margin:0px;height:100%"><iframe id="main-iframe" src="/_Incapsula_Resource?SWUDNSAI=31&xinfo=7-76038078-0%20NNNN%20RT%281681371500126%20883769%29%20q%280%20-1%20-1%20-1%29%20r%281%20-1%29%20B12%2814%2c0%2c0%29%20U24&incident_id=434000870345502677-416622015402874311&edet=12&cinfo=0e0000007628&rpinfo=0&cts=DPikR6GJMIFv5EZViA7marrlwuB%2fm2hm0anNDYgXYljRyMxnZbUSqa%2f0%2fYejjUwz&mth=GET" frameborder=0 width="100%" height="100%" marginheight="0px" marginwidth="0px">Request unsuccessful. Incapsula incident ID: 434000870345502677-416622015402874311</iframe></body></html>'
    data = '<html style="height:100%"><head><META NAME="ROBOTS" CONTENT="NOINDEX, NOFOLLOW"><meta name="format-detection" content="telephone=no"><meta name="viewport" content="initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"><script type="text/javascript" src="/_Incapsula_Resource?SWJIYLWA=719d34d31c8e3a6e6fffd425f7e032f3"></script><script src="/rtaliuery-Doct-The-Then-throngling-Was-Son-Hes-I" async></script></head><body style="margin:0px;height:100%"><iframe id="main-iframe" src="/_Incapsula_Resource?SWUDNSAI=31&xinfo=8-42044191-0%20NNNY%20RT%281681712702480%2080751%29%20q%280%20-1%20-1%201%29%20r%280%20-1%29%20B12%2814%2c0%2c0%29%20U24&incident_id=725000940485406716-293138054939744136&edet=12&cinfo=0e000000f628&rpinfo=0&cts=Sc2J61I0jK02jnVhOzboC5GjLWSptKvEijNpIzefc1NdtBv1SFKT8DPIYfdB35wh&mth=GET" frameborder=0 width="100%" height="100%" marginheight="0px" marginwidth="0px">Request unsuccessful. Incapsula incident ID: 725000940485406716-293138054939744136</iframe></body></html>'
    geet(data)
    pass
