# -*- coding:utf-8 -*-

# 题目描述
# 输入一个整数，输出该数制表示中1的个数。其中负数用补码表示。
#  @href https://www.nowcoder.com/practice/8ee967e43c2c4ec193b040ea7fbb10b8


class Solution:

    def NumberOf1(self, n):
        return bin(n & 0xffffffff).count('1')


s = Solution()
print(s.NumberOf1(-10))




