# -*- coding:utf-8 -*-

"""
最小的K个数

题目描述:  *** 时间效率
    输入n个整数，找出其中最小的K个数。

输入描述:
    例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

    输出需要 从小到大 排序

    @href https://www.nowcoder.com/practice/6a296eb82cf844ca8539b57c23e6e9bf
"""


class Solution:

    def GetLeastNumbers_Solution(self, tinput, k):
        if k <= 0 or k > len(tinput):
            return []

        result = [None] * k
        for n in tinput:
            self.minInsert(result, n)

        return result

    def minInsert(self, result, n):
        for i in range(len(result)):
            if result[i] is None:
                result[i] = n
                break
            elif result[i] > n:
                result.insert(i, n)
                result.pop()
                break


s = Solution()
print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8], 7))

