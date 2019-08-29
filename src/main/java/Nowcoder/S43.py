# -*- coding:utf-8 -*-
"""
题目描述
    汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果
    。对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
    例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！

    @href https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec
"""


class Solution:

    def LeftRotateString(self, s, n):
        if s == "":
            return ""
        n = n % len(s)
        return s[n:]+s[:n]


s = Solution()
print("✌️✌️✌️✌️✌️✌️")
print(s.LeftRotateString("abcXYZdef", 3))

