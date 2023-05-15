# @author: 矩阵算法
# @file: 2023/3/31
# time: 2023-03-31 17:59


# 横坐标为x,纵坐标为y
def main_method(list_):
    changdu = len(list_) - 1
    xiaochangdu = len(list_[0]) - 1
    for x in range(7):
        for y in range(5):
            # 获取该坐标点的颜色
            c = list_[y][x]
            # 判断该坐标向右移是否满足(考虑越界问题，需判断坐标变换后是否在矩阵内)
            if ((y - 1) >= 0 and (x + 1) <= xiaochangdu and (
                    y + 1) <= changdu and list_[y - 1][x + 1] == c and list_[y + 1][x + 1] == c) or (
                    (x + 2) <= xiaochangdu and (x + 3) <= xiaochangdu and list_[y][x + 2] == c and list_[y][
                x + 3] == c) or (
                    (y - 1) >= 0 and (x + 1) <= xiaochangdu and (
                    y - 2) >= 0 and list_[y - 1][x + 1] == c and list_[y - 2][x + 1] == c) or (
                    (y + 1) <= changdu and (x + 1) <= xiaochangdu and (
                    y + 2) <= changdu and list_[y + 1][x + 1] == c and list_[y + 2][x + 1] == c):
                return [[x, y], [x + 1, y]]
            # 判断该坐标向左移是否满足
            elif ((y - 1) >= 0 and (x - 1) >= 0 and (
                    y + 1) <= changdu and list_[y - 1][x - 1] == c and list_[y + 1][x - 1] == c) or (
                    (x - 2) >= 0 and (x - 3) >= 0 and list_[y][x - 2] == c and list_[y][x - 3] == c) or (
                    (y - 1) >= 0 and (x - 1) >= 0 and (
                    y - 2) >= 0 and list_[y - 1][x - 1] == c and list_[y - 2][x - 1] == c) or (
                    (y + 1) <= changdu and (x - 1) >= 0 and (
                    y + 2) <= changdu and list_[y + 1][x - 1] == c and list_[y + 2][x - 1] == c):
                return [[x, y], [x - 1, y]]
            # 判断该坐标向上移是否满足
            elif ((y - 1) >= 0 and (x - 1) >= 0 and (
                    x + 1) <= xiaochangdu and list_[y - 1][x - 1] == c and list_[y - 1][x + 1] == c) or (
                    (y - 2) >= 0 and (y - 3) >= 0 and list_[y - 2][x] == c and list_[y - 3][x] == c) or (
                    (y - 1) >= 0 and (x - 1) >= 0 and (
                    x - 2) >= 0 and list_[y - 1][x - 1] == c and list_[y - 1][x - 2] == c) or (
                    (x + 1) <= xiaochangdu and (x + 2) <= xiaochangdu and (
                    y - 1) >= 0 and list_[y - 1][x + 1] == c and list_[y - 1][x + 2] == c):
                return [[x, y], [x, y - 1]]
            # 判断该坐标向下移是否满足
            elif ((y + 1) <= changdu and (x - 1) >= 0 and (
                    x + 1) <= xiaochangdu and list_[y + 1][x - 1] == c and list_[y + 1][x + 1] == c) or (
                    (y + 2) <= changdu and (y + 3) <= changdu and list_[y + 2][x] == c and list_[y + 3][x] == c) or (
                    (y + 1) <= changdu and (x - 1) >= 0 and (
                    x - 2) >= 0 and list_[y + 1][x - 1] == c and list_[y + 1][x - 2] == c) or (
                    (x + 1) <= xiaochangdu and (x + 2) <= xiaochangdu and (
                    y + 1) <= changdu and list_[y + 1][x + 1] == c and list_[y + 1][x + 2] == c):
                return [[x, y], [x, y + 1]]
    return []


if __name__ == '__main__':
    list_ = [
        [
            0,
            0,
            0,
            4,
            0
        ],
        [
            0,
            0,
            3,
            0,
            0
        ],
        [
            0,
            0,
            0,
            0,
            0
        ],
        [
            0,
            0,
            0,
            0,
            1
        ],
        [
            1,
            1,
            1,
            0,
            1
        ]
    ]
    print(main_method(list_))
