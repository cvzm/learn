# -*- coding:utf-8 -*-

# 题目描述
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
# 所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
#  @href https://www.nowcoder.com/practice/beb5aa231adc45b2a5dcc5b62c93f593


class Solution:

    def reOrderArray(self, array):
        odd = []
        even = []
        for i in array:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return odd + even


s = Solution()
print(s.reOrderArray([1, 2, 3, 4, 5, 6, 7]))




