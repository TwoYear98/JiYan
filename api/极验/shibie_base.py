# @author: shibie_base
# @file: 2023/4/17
# time: 2023-04-17 13:37
import base64
import json

import requests


def base64_api(img_url):
    res = requests.get(img_url).content
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


def get_click_xy(img_url):
    content = (base64_api("https://static.geetest.com" + img_url))
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
