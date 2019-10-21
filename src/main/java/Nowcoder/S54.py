# -*- coding:utf-8 -*-
"""
题目描述
    请实现一个函数用来找出字符流中第一个只出现一次的字符。
    例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
    当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
    如果当前字符流没有存在出现一次的字符，返回#字符。

    @href https://www.nowcoder.com/practice/00de97733b8e4f97a3fb5c680ee10720
"""
class Solution:

    def __init__(self):
        self.char_count = {}
        self.char_list = []

    def FirstAppearingOnce(self):
        for key in self.char_list:
            if self.char_count[key] == 1:
                return key
        return '#'

    def Insert(self, char):
        self.char_count[char] = 1 if char not in self.char_count else self.char_count[char]+1
        self.char_list.append(char)


s = Solution()
print("ok")

