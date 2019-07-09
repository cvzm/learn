# -*- coding:utf-8 -*-

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
    @href https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993
"""

# 放在方法内，会拖累性能
from functools import cmp_to_key

class Solution:

    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        compare = cmp_to_key(lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x)))
        cur = sorted(numbers, key=compare)
        return "".join(str(s) for s in cur)

s = Solution()
print(s.PrintMinNumber([3, 32, 321]))

