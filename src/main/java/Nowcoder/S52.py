# -*- coding:utf-8 -*-
"""
题目描述
    请实现一个函数用来匹配包括'.'和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
    在本题中，匹配是指字符串的所有字符匹配整个模式。
    例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配

    @href https://www.nowcoder.com/practice/45327ae22b7b413ea21df13ee7d6429c
"""
class Solution:

    # s, pattern都是字符串
    def match(self, s, pattern):
        if not pattern:
            if not s:
                return True
            return False

        if not s:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s, pattern[2:])
            return False

        # pattern的第二个字符为*的情况
        if len(pattern) > 1 and pattern[1] == '*':
            # s与pattern的第一个元素不同，则s不变，pattern后移两位
            if s[0] != pattern[0] and pattern[0] != '.':
                return self.match(s, pattern[2:])

            # 如果s[0]与pattern[0]相同，且pattern[1]为*，这个时候有三种情况
            # pattern后移2个，s不变；相当于把pattern前两位当成空，匹配后面的
            # pattern后移2个，s后移1个；相当于pattern前两位与s[0]匹配
            # pattern不变，s后移1个；相当于pattern前两位，与s中的多位进行匹配，因为*可以匹配多位
            return self.match(s, pattern[2:]) \
                        or self.match(s[1:], pattern[2:]) \
                        or self.match(s[1:], pattern)

        # pattern第二个字符不为*的情况
        if s[0] == pattern[0] or pattern[0] == '.':
            return self.match(s[1:], pattern[1:])

        return False


s = Solution()
print(s.match("aaac","ab*ac*a."))
print(s.match("aaaabc","a*b*c*abc"))
print("ok")
