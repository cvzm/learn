# -*- coding:utf-8 -*-

"""
连续子数组的最大和

    @href https://www.nowcoder.com/practice/459bd355da1549fa8a49e350bf3df484
"""


class Solution:

    def FindGreatestSumOfSubArray(self, array):
        if array is None or len(array) == 0:
            return None
        maxSum = array[0]
        tempSum = array[0]
        for a in array[1:]:
            tempSum = max(tempSum + a, a)
            maxSum = max(maxSum, tempSum)
        return maxSum


s = Solution()
print(s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))

