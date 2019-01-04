# description: 偷窥到的密码
# author: C.v.
# href: https://www.codewars.com/kata/5263c6999e0f40dee200059d
# date: 2019-1-3


# 减少import的模块
# import itertools
from itertools import product

# # 每个数对应的可能性集合
# plate = [
#     [0, 8],
#     [1, 2, 4],
#     [2, 3, 5,1],
#     [3, 6, 2],
#     [4, 1, 5, 7],
#     [5, 2, 6, 8, 4],
#     [6, 3, 9, 5],
#     [7, 4, 8],
#     [8, 5, 9, 0, 7],
#     [9, 6, 8]
# ]
#
#
# def get_pins(observed):
#     temp = []
#     for i in range(len(observed)):
#         temp.append([])
#         for j in plate[int(observed[i])]:
#             temp[i].append(str(j))
#
#     # 两种转换方式均可
#     # return ["".join(i) for i in itertools.product(*temp)]
#     return list(map("".join, product(*temp)))
#
#
# print(get_pins("11"))


# 优化后。 减少没必要的for
plate = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')


def get_pins(observed):
    return list(map("".join, product(*(plate[int(i)] for i in observed))))


print(get_pins("11"))

