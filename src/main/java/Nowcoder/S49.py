# -*- coding:utf-8 -*-
"""
题目描述
    将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，
    要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0。

    @href https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e
"""

class Solution:

    number = {str(num): num for num in range(10)}

    positive, minus = '+', '-'

    def StrToInt(self, s):
        # 标记 正数(True) or 负数(False)
        sign = True
        # 标记是否开始数字，用于校验开头符号(可能多个)
        is_start_num = False
        # 返回结果
        res = 0

        for c in s:
            # 校验是否开始数字， 未开始数字前先校验符号
            if not is_start_num:
                # 校验 sign
                if c in [self.positive, self.minus]:
                    # 转译 +，- 为 true，false
                    # temp = c == self.positive
                    # sign = temp if sign else not temp

                    # 合并上两行代码
                    sign = c == self.positive if sign else c == self.minus
                    continue
            # 校验是否为数字
            if self.number.get(c) is None:
                return 0

            res *= 10
            res += self.number.get(c)

        return res if sign else -res



        # print(self.num)

s = Solution()
print(s.StrToInt("++213"))
print(s.StrToInt("---2aa"))
print(s.StrToInt("-123"))
print("ok")