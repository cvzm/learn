# -*- coding:utf-8 -*-
"""
题目描述
    牛客最近来了一个新员工Fish，每天早晨总是会拿着一本英文杂志，写些句子在本子上。
    同事Cat对Fish写的内容颇感兴趣，有一天他向Fish借来翻看，但却读不懂它的意思。例如，“student. a am I”。
    后来才意识到，这家伙原来把句子单词的顺序翻转了，正确的句子应该是“I am a student.”。
    Cat对一一的翻转这些单词顺序可不在行，你能帮助他么？

    @href https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3
"""


class Solution:

    # 分割符号
    format = " "

    def ReverseSentence(self, s):
        res = ""
        for a in s.split(self.format)[::-1]:
            res += a + self.format
        return res[:-1]


s = Solution()
print("✌️✌️✌️✌️✌️✌️")
print(s.ReverseSentence("student. a am I"))
print(s.ReverseSentence("I am a student."))
print(s.ReverseSentence("Wonderful"))

