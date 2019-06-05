# -*- coding:utf-8 -*-

"""
题目描述:
    输入一个字符串,按字典序打印出该字符串中字符的所有排列。
    例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:
    输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

    @href https://www.nowcoder.com/practice/fe6b651b66ae47d7acce78ffdd9a96c7
"""


class Solution:

    def Permutation(self, ss):
        result = []
        self.append(ss, "", result)
        return result

    def append(self, ss, prefix, res):
        if len(ss) == 1:
            return res.append(prefix + ss)
        for i in range(len(ss)):
            # 去重
            if i != 0 and ss[i] == ss[i-1]:
                continue
            self.append(ss[:i] + ss[i+1:], prefix + ss[i], res)


s = Solution()
# print(s.Permutation("abc"))
print(s.Permutation("aaab"))

