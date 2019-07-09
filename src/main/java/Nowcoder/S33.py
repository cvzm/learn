# -*- coding:utf-8 -*-

"""

把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
    @href https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b
"""


class Solution:

    def GetUglyNumber_Solution(self, index):
        if index < 7:
            return index
        res = [1]
        t2 = t3 = t5 = 0
        for i in range(1, index):
            s2, s3, s5 = res[t2] * 2, res[t3] * 3, res[t5] * 5
            m = min(s2, s3, s5)
            res.append(m)
            # 利用  False/True 运算自动对应 0/1 的特性
            t2 += m == s2
            t3 += m == s3
            t5 += m == s5

        return res[index - 1]


s = Solution()
print(s.GetUglyNumber_Solution(41))

