# -*- coding:utf-8 -*-
"""
统计一个数字在排序数组中出现的次数。
    @href https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2
"""


class Solution:

    def GetNumberOfK(self, data, k):
        end = self.biSearchEnd(data, k)
        if end == -1:
            return 0
        return end - self.biSearchStart(data, k) + 1

    # 二分找到第一个满足元素下标
    def biSearchStart(self, data, k):
        size = len(data)
        start, end = 0, size - 1
        while start <= end:
            mid = int((start + end) / 2)
            if data[mid] == k:
                if mid == 0 or data[mid - 1] != k:
                    return mid
                end = mid - 1
            elif k > data[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    # 二分找到最后一个满足元素下标
    def biSearchEnd(self, data, k):
        size = len(data)
        start, end = 0, size - 1
        while start <= end:
            mid = (start + end) // 2
            if data[mid] == k:
                if mid == size-1 or data[mid + 1] != k:
                    return mid
                start = mid + 1
            elif k > data[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


s = Solution()
print(s.GetNumberOfK([1,2,3,3,3,3,4,5], 3))
