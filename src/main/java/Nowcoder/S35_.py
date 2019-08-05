# -*- coding:utf-8 -*-
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P
    @href https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5
"""


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs(self, data):
        # write code here
        if len(data) < 2: return 0
        self.mergeSort(data)
        return self.count % 1000000007

    def mergeSort(self, data):
        if len(data) < 2: return data
        mid = len(data)//2
        left = self.mergeSort(data[:mid])
        right = self.mergeSort(data[mid:])
        i, j = 0, 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
                self.count += (len(left)-i)
        return res + left[i:] + right[j:]
