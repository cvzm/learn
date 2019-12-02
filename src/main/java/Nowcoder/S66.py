# -*- coding:utf-8 -*-
"""
    地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
    但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
    但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

    @href https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc
"""


class Solution:

    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        entry = [[0 for i in range(cols)] for j in range(rows)]
        self.move(threshold, rows, cols, entry, 0, 0)

        return self.count

    def move(self, threshold, rows, cols, entry, x, y):
        if x < 0 or y < 0 or x > rows - 1 or y > cols - 1:
            return
        if entry[x][y] == 1:
            return
        if x // 10 + x % 10 + y // 10 + y % 10 > threshold:
            return
        entry[x][y] = 1
        self.count += 1
        self.move(threshold, rows, cols, entry, x - 1, y)
        self.move(threshold, rows, cols, entry, x, y - 1)
        self.move(threshold, rows, cols, entry, x + 1, y)
        self.move(threshold, rows, cols, entry, x, y + 1)