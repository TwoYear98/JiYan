# @author: 消消乐矩阵算法
# @file: 2023/3/31
# time: 2023-03-31 14:10
import numpy as np


def juzhen_suanfa(matrix):
    matrix = np.array(matrix)
    list_ = np.transpose(matrix)  # 转换矩阵，行变列，列变行

    for x in range(3):
        for y in range(3):
            # 获取该坐标点的颜色
            c = list_[y][x]
            # 判断该坐标向右移是否满足(考虑越界问题，需判断坐标变换后是否在矩阵内)
            if ((y - 1) >= 0 and (x + 1) <= 2 and (
                    y + 1) <= 2 and list_[y - 1][x + 1] == c and list_[y + 1][x + 1] == c) or (
                    (x + 2) <= 2 and (x + 3) <= 2 and list_[y][x + 2] == c and list_[y][x + 3] == c) or (
                    (y - 1) >= 0 and (x + 1) <= 2 and (
                    y - 2) >= 0 and list_[y - 1][x + 1] == c and list_[y - 2][x + 1] == c) or (
                    (y + 1) <= 2 and (x + 1) <= 2 and (
                    y + 2) <= 2 and list_[y + 1][x + 1] == c and list_[y + 2][x + 1] == c):
                return [[x, y], [x + 1, y]]
            # 判断该坐标向左移是否满足
            elif ((y - 1) >= 0 and (x - 1) >= 0 and (
                    y + 1) <= 2 and list_[y - 1][x - 1] == c and list_[y + 1][x - 1] == c) or (
                    (x - 2) >= 0 and (x - 3) >= 0 and list_[y][x - 2] == c and list_[y][x - 3] == c) or (
                    (y - 1) >= 0 and (x - 1) >= 0 and (
                    y - 2) >= 0 and list_[y - 1][x - 1] == c and list_[y - 2][x - 1] == c) or (
                    (y + 1) <= 2 and (x - 1) >= 0 and (
                    y + 2) <= 2 and list_[y + 1][x - 1] == c and list_[y + 2][x - 1] == c):
                return [[x, y], [x - 1, y]]
            # 判断该坐标向上移是否满足
            elif ((y - 1) >= 0 and (x - 1) >= 0 and (
                    x + 1) <= 2 and list_[y - 1][x - 1] == c and list_[y - 1][x + 1] == c) or (
                    (y - 2) >= 0 and (y - 3) >= 0 and list_[y - 2][x] == c and list_[y - 3][x] == c) or (
                    (y - 1) >= 0 and (x - 1) >= 0 and (
                    x - 2) >= 0 and list_[y - 1][x - 1] == c and list_[y - 1][x - 2] == c) or (
                    (x + 1) <= 2 and (x + 2) <= 2 and (
                    y - 1) >= 0 and list_[y - 1][x + 1] == c and list_[y - 1][x + 2] == c):
                return [[x, y], [x, y - 1]]
            # 判断该坐标向下移是否满足
            elif ((y + 1) <= 2 and (x - 1) >= 0 and (
                    x + 1) <= 2 and list_[y + 1][x - 1] == c and list_[y + 1][x + 1] == c) or (
                    (y + 2) <= 2 and (y + 3) <= 2 and list_[y + 2][x] == c and list_[y + 3][x] == c) or (
                    (y + 1) <= 2 and (x - 1) >= 0 and (
                    x - 2) >= 0 and list_[y + 1][x - 1] == c and list_[y + 1][x - 2] == c) or (
                    (x + 1) <= 2 and (x + 2) <= 2 and (
                    y + 1) <= 2 and list_[y + 1][x + 1] == c and list_[y + 1][x + 2] == c):
                return [[x, y], [x, y + 1]]
            else:
                continue
    return []


if __name__ == '__main__':
    matrix = [
        [
            2,
            2,
            0
        ],
        [
            1,
            3,
            0
        ],
        [
            2,
            1,
            1
        ]
    ]
    print("原始矩阵：", matrix, sep='\n')
    print("转置矩阵：", juzhen_suanfa(matrix), sep='\n')
