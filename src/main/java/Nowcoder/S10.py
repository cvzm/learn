# -*- coding:utf-8 -*-

# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
#  @href https://www.nowcoder.com/practice/72a5a919508a4251859fb2cfb987a0e6


class Solution:

    result = [0, 1, 2, 3]

    def rectCover(self, n):
        size = len(Solution.result) - 1
        if size > n:
            return Solution.result[n]
        for i in range(size, n):
            Solution.result.append(Solution.result[i-1] + Solution.result[i])
        return Solution.result[n]




