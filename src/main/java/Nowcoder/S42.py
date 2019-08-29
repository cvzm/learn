# -*- coding:utf-8 -*-
"""
题目描述
    输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
    如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
    对应每个测试案例，输出两个数，小的先输出。

    @href https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe
"""


class Solution:

    def FindNumbersWithSum(self, array, tsum):
        if len(array) == 0 or tsum == 0:
            return []
        left = 0
        right = left + 1
        while array[right] <= tsum:
            total = array[left] + array[right]
            if total < tsum and right < len(array):
                right += 1
            else:
                if total == tsum:
                    return [array[left], array[right]]
                left += 1
                right = left + 1
        return []


s = Solution()
print("✌️✌️✌️✌️✌️✌️")
print(s.FindNumbersWithSum([1,2,4,7,11,15], 15))

