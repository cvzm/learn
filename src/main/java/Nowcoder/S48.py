# -*- coding:utf-8 -*-
"""
题目描述
    写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

    @href https://www.nowcoder.com/practice/59ac416b4b944300b617d4f7f111b215
"""

class Solution:

    def Add(self, num1, num2):
        import ctypes
        while num1 != 0:
            num1, num2 = ctypes.c_int32(num1 & num2).value << 1, \
                         num1 ^ num2
        return num2


s = Solution()
print(s.Add(1, 2))
print(s.Add(111, 899))
print(s.Add(1, -2))
print(s.Add(3, 0))
print(s.Add(0, -4))
print(s.Add(-2, -8))
print(s.Add(-1, 2))
print("ok")