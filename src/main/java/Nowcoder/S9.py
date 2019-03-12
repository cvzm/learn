# -*- coding:utf-8 -*-

# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
#  @href https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387


class Solution:

    result = [0, 1, 2]

    def jumpFloorII(self, n):
        size = len(Solution.result) - 1
        if size > n:
            return Solution.result[n]
        for i in range(size, n):
            Solution.result.append(2 * Solution.result[i])
        return Solution.result[n]


s = Solution()
print(s.jumpFloorII(9))


