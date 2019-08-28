# -*- coding:utf-8 -*-
"""
题目描述
    小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
    但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
    没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
    现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
    输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

    @href https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe
"""


class Solution:

    # 初始值
    START = 1
    # 等差值
    DEVIATION = 1

    def FindContinuousSequence(self, tsum):
        left = self.START
        right = left + self.DEVIATION
        total = left + right
        # 中位数
        median = tsum / 2 + 1
        result = []
        while left < median:
            if total < tsum:
                right += self.DEVIATION
            else:
                if total == tsum:
                    print("✌️✌️✌️✌️✌️✌️")
                    result.append([left, right])
                left += self.DEVIATION
                right = left + self.DEVIATION

            total = self.summation(left, right)

        return self.resFormat(result)

    # 求和
    def summation(self, a, b):
        return int((a + b) * (b - a + 1) / 2)

    # 处理输出格式, 还原数列
    def resFormat(self, result):
        for res in result:
            a = res[0]
            b = res[1]

            # python 2.7
            # res *= 0
            # python 3.7
            res.clear()
            for i in range(a, b + 1):
                res.append(i)
        return result


s = Solution()
print(s.FindContinuousSequence(3))

