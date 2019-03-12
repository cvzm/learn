# -*- coding:utf-8 -*-

# 题目描述
# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#  @href https://www.nowcoder.com/practice/1a834e5e3e1a4b7ba251417554e07c00


class Solution:

    def Power(self, base, exponent):
        # return pow(base, exponent)
        if exponent < 0:
            exponent = exponent * -1
            base = 1 / base
        res = 1
        for i in range(exponent):
            res = res * base
        return res


s = Solution()
print(s.Power(2, -3))




