# -*- coding:utf-8 -*-
"""
题目描述
    如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
    那么中位数就是所有数值排序之后位于中间的数值。
    如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
    我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。

    @href https://www.nowcoder.com/practice/9be0172896bd43948f8a32fb954e1be1
"""


class Solution:

    arr = []

    def Insert(self, num):
        for i in range(len(self.arr)):
            if self.arr[i] > num:
                self.arr.insert(i, num)
                return
        self.arr.append(num)

    def GetMedian(self, bug):
        k = len(self.arr) / 2
        if k * 2 == len(self.arr):
            return float(self.arr[k] + self.arr[k-1]) / 2
        return self.arr[k]


s = Solution()
s.Insert(4)
s.Insert(2)
s.Insert(6)
s.Insert(8)
s.Insert(3)
s.Insert(7)
s.GetMedian('bug')
print("ok")

