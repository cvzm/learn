# -*- coding:utf-8 -*-

"""
题目描述
    输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
    例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
    @href https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a
"""
# 1   2   3   4
# 5   6   7   8
# 9   10  11  12


class Solution:

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        x, y = len(matrix[0]), len(matrix)
        start = 0
        printNums = []
        while x > start * 2 and y > start * 2:
            self.printingCore(matrix, x, y, start, printNums)
            start += 1
        return printNums

    # 处理打印
    def printingCore(self, matrix, x, y, start, printNums):
        endX = x - 1 - start
        endY = y - 1 - start
        # 从左到右
        for i in range(start, endX + 1):
            printNums.append(matrix[start][i])
        if start < endY:
            # 从上到下
            for i in range(start + 1, endY + 1):
                printNums.append(matrix[i][endX])
            # 从右到左
            for i in range(endX - 1, start - 1, -1):
                printNums.append(matrix[endY][i])
        if start < endX:
            # 从下到上
            for i in range(endY - 1, start, -1):
                printNums.append(matrix[i][start])
        return printNums


s = Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
matrix = [[1,2],[3,4]]
matrix = [[1],[2],[3],[4],[5]]
p = s.printMatrix(matrix)
print(p)





