# @author: huanjing
# @file: 2023/4/14
# time: 2023-04-14 16:21
import random
import time

from 极验.极验三代点选.极验三代点选 import get_random


def get_huanjing():
    huanjing_dict = {
        "STYLE": 1,
        "SCRIPT": random.randint(1, 10),
        "DIV": random.randint(10, 20),
        "P": 3,
        "SPAN": 1,
        "A": 1,
        "textLength": random.randint(10000, 15000),
        "HTMLLength": random.randint(10000, 15000),
        "documentMode": "CSS1Compat",
        "browserLanguage": "zh-CN",
        "browserLanguages": "zh-CN,zh",
        "devicePixelRatio": 1,
        "colorDepth": random.randint(20, 24),
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "cookieEnabled": 1,
        "netEnabled": 1,
        "innerWidth": 1920,
        "innerHeight": random.randint(100, 300),
        "outerWidth": 1920,
        "outerHeight": random.randint(1000, 1200),
        "screenWidth": 1920,
        "screenHeight": 1080,
        "screenAvailWidth": 1920,
        "screenAvailHeight": random.randint(1000, 1200),
        "screenLeft": -1920,
        "screenTop": 0,
        "screenAvailLeft": -1920,
        "screenAvailTop": 0,
        "localStorageEnabled": random.randint(0, 1),
        "sessionStorageEnabled": random.randint(0, 1),
        "indexedDBEnabled": random.randint(0, 1),
        "platform": "Win32",
        "doNotTrack": 0,
        "timezone": -8,
        # "canvas2DFP": "2d7a3f4ebbe8b0c8b98a595e5ef5d1fe",
        "canvas2DFP": get_random() + get_random(),
        "canvas3DFP": 0,
        "plugins": "internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer",
        "maxTouchPoints": 20,
        "flashEnabled": -1,
        "javaEnabled": 0,
        "hardwareConcurrency": 8,
        "jsFonts": "Arial,ArialBlack,ArialNarrow,Calibri,Cambria,CambriaMath,ComicSansMS,Consolas,Courier,CourierNew,Georgia,Helvetica,Impact,LucidaConsole,LucidaSansUnicode,MicrosoftSansSerif,MSGothic,MSPGothic,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings",
        "mediaDevices": -1,
        "timestamp": int(time.time() * 1000),
        "touchEvent": -1,
        "performanceTiming": -1,
        "internalip": -1
    }
    huanjing_list = [
        "textLength",
        "HTMLLength",
        "documentMode",
        "A",
        "ARTICLE",
        "ASIDE",
        "AUDIO",
        "BASE",
        "BUTTON",
        "CANVAS",
        "CODE",
        "IFRAME",
        "IMG",
        "INPUT",
        "LABEL",
        "LINK",
        "NAV",
        "OBJECT",
        "OL",
        "PICTURE",
        "PRE",
        "SECTION",
        "SELECT",
        "SOURCE",
        "SPAN",
        "STYLE",
        "TABLE",
        "TEXTAREA",
        "VIDEO",
        "screenLeft",
        "screenTop",
        "screenAvailLeft",
        "screenAvailTop",
        "innerWidth",
        "innerHeight",
        "outerWidth",
        "outerHeight",
        "browserLanguage",
        "browserLanguages",
        "systemLanguage",
        "devicePixelRatio",
        "colorDepth",
        "userAgent",
        "cookieEnabled",
        "netEnabled",
        "screenWidth",
        "screenHeight",
        "screenAvailWidth",
        "screenAvailHeight",
        "localStorageEnabled",
        "sessionStorageEnabled",
        "indexedDBEnabled",
        "CPUClass",
        "platform",
        "doNotTrack",
        "timezone",
        "canvas2DFP",
        "canvas3DFP",
        "plugins",
        "maxTouchPoints",
        "flashEnabled",
        "javaEnabled",
        "hardwareConcurrency",
        "jsFonts",
        "timestamp",
        "performanceTiming",
        "internalip",
        "mediaDevices",
        "DIV",
        "P",
        "UL",
        "LI",
        "SCRIPT",
        "touchEvent"
    ]
    dd = []
    for hj in huanjing_list:
        try:
            dd.append(huanjing_dict[hj])
        except:
            dd.append("-1")
    result_text = ""
    for i in dd:
        result_text += str(i) + "!!"
    return result_text[:-2]

if __name__ == '__main__':
    print(get_huanjing())