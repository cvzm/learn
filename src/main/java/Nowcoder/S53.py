# -*- coding:utf-8 -*-
"""
题目描述
    请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。

    @href https://www.nowcoder.com/practice/6f8c901d091949a5837e24bb82a731f2
"""
class Solution:

    # s字符串
    def isNumeric(self, s):
        # e后面要跟数字, 或者负数， 单不能为小数
        if not s:
            return False

        # 记录是否出现过小数、e、+-
        have_decimal = False
        have_e = False
        have_sign = False

        # 当前扫描下标
        index = 0
        while index < len(s):
            c = s[index]

            if s[index] == '+' or s[index] == '-':
                # 第一次出现， 只能是 首位 或者 前一位是e
                if not have_sign and index > 0 and not self.is_e(s[index-1]):
                    return False
                # 第二次出现， 只能是 前一位是e
                if have_sign and not self.is_e(s[index-1]):
                    return False

                have_sign = True

            elif c == '.':
                # 校验是否只出现 一次小数点, 并且不能出现在e后面
                if have_decimal or have_e:
                    return False

                have_decimal = True

            elif self.is_e(c):
                # e 不能是首位，且前一位必须是数字，  不能是 末尾
                if index == 0 or not self.is_number(s[index - 1]) or index == len(s) - 1:
                    return False
                # 校验e出现次数
                if have_e:
                    return False

                have_e = True

            elif not self.is_number(c):
                # 排除不是数字的情况
                return False

            index += 1

        return True

    # 校验字符是否为数字
    def is_number(self, c):
        return '0' <= c <= '9'

    # 校验字符是否为e
    def is_e(self, c):
        return c == 'e' or c == 'E'


s = Solution()
print(s.isNumeric("100e"))
print("ok")

