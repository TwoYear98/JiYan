# -*- coding: utf-8 -*-
import random


def guiji_eny(e):
    r = []
    s = 0
    o = 0
    a = len(e) - 1
    while o < a:
        t = round(e[o + 1][0] - e[o][0])
        n = round(e[o + 1][1] - e[o][1])
        i = round(e[o + 1][2] - e[o][2])
        if t == 0 and n == 0 and i == 0:
            pass
        elif t == 0 and n == 0:
            s += i
        else:
            r.append([t, n, i + s])
            s = 0
        o += 1

    if s != 0:
        r.append([t, n, s])

    return r


def __ease_out_expo(x):
    if x == 1:
        return 1
    else:
        return 1 - pow(2, -10 * x)


def __ease_out_quart(x):
    return 1 - pow(1 - x, 4)


def get_slide_track(distance):
    """
    根据滑动距离生成滑动轨迹
    :param distance: 需要滑动的距离
    :return: 滑动轨迹<type 'list'>: [[x,y,t], ...]
        x: 已滑动的横向距离
        y: 已滑动的纵向距离, 除起点外, 均为0
        t: 滑动过程消耗的时间, 单位: 毫秒
    """

    if not isinstance(distance, int) or distance < 0:
        raise ValueError(f"distance类型必须是大于等于0的整数: distance: {distance}, type: {type(distance)}")
    # 初始化轨迹列表
    slide_track = [
        [random.randint(30, 60), random.randint(100, 150), 0]
    ]
    # 共记录count次滑块位置信息
    count = 30 + int(distance / 2)
    # 初始化滑动时间
    # 记录上一次滑动的距离
    _x = 0
    _y = 0
    _t = 0
    for i in range(count):
        # 已滑动的横向距离
        x = round(__ease_out_expo(i / count) * distance)
        # 滑动过程消耗的时间
        t = random.randint(20, 30)
        # slide_track.append([x - _x, _y, t])
        slide_track.append([x, _y, _t])
        _x = x
        _t += t
    return guiji_eny(slide_track)


if __name__ == '__main__':
    slide_track = get_slide_track(102)
    print(slide_track)
    print(len(slide_track))
