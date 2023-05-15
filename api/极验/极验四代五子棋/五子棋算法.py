# @author: 消消乐矩阵算法
# @file: 2023/3/31
# time: 2023-03-31 14:10


def juzhen_suanfa(ques):
    # 横向查找
    def check_x(matrix):
        for index1, array1 in enumerate(matrix):
            unique_list = list(set(array1))
            four_num = [x for x in unique_list if array1.count(x) == 4 and x != 0]
            if four_num:
                one_num = [x for x in unique_list if array1.count(x) == 1]
                one_num_index = array1.index(one_num[0])
                for index2, array2 in enumerate(matrix):
                    for arr in array2:
                        if four_num[0] == arr and index2 != index1:
                            arr_index = array2.index(arr)
                            return [[index2, arr_index], [index1, one_num_index]]

    # 纵向查找
    def check_y(matrix):
        transposition_array = list(map(list, zip(*matrix)))
        x_result = check_x(transposition_array)
        if x_result:
            actual_result = [[x_result[0][1], x_result[0][0]], [x_result[1][1], x_result[1][0]]]
            return actual_result

    # 对角查找 从左到右
    def check_left_to_right(matrix):
        array_left_to_right = []
        for index1, array1 in enumerate(matrix):
            array_left_to_right.append(array1[index1])
        unique_list = list(set(array_left_to_right))
        four_num = [x for x in unique_list if array_left_to_right.count(x) == 4 and x != 0]
        if four_num:
            one_num = [x for x in unique_list if array_left_to_right.count(x) == 1]
            one_num_index = array_left_to_right.index(one_num[0])
            for index2, array2 in enumerate(matrix):
                for index3, array3 in enumerate(array2):
                    if four_num[0] == array3 and index2 != index3:
                        return [[index2, index3], [one_num_index, one_num_index]]

    def check_right_to_left(matrix):
        reverse_matrix = [x[::-1] for x in matrix]
        res = check_left_to_right(reverse_matrix)
        actual_result = []
        matrix_dict = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0}
        for i in res:
            actual_result.append([i[0], matrix_dict[i[1]]])
        return actual_result

    result = check_x(ques)
    if not result:
        result = check_y(ques)
    if not result:
        result = check_left_to_right(ques)
    if not result:
        result = check_right_to_left(ques)
    return result


if __name__ == '__main__':
    matrix = [[1, 2, 2, 2, 2],
              [0, 1, 4, 2, 0],
              [4, 2, 1, 2, 4],
              [4, 3, 2, 0, 1],
              [2, 3, 3, 3, 1]]

    print("原始矩阵：", matrix, sep='\n')
    print("转置矩阵：", juzhen_suanfa(matrix), sep='\n')
