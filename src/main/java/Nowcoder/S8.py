# -*- coding:utf-8 -*-

# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
#  @href https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4


class Solution:

    result = [0, 1, 2]

    def jumpFloor(self, n):
        size = len(Solution.result) - 1
        if size > n:
            return Solution.result[n]
        for i in range(size, n):
            Solution.result.append(Solution.result[i-1] + Solution.result[i])
        return Solution.result[n]


s = Solution()
print(s.jumpFloor(9))


