# -*- coding:utf-8 -*-

# 题目描述
#  大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
#  @href https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3


class Solution:

    result = [0, 1, 1]

    def Fibonacci(self, n):
        size = len(Solution.result) - 1
        if size > n:
            return Solution.result[n]
        a, b = Solution.result[size-1], Solution.result[size]
        while len(Solution.result) <= n:
            a, b = b, a+b
            Solution.result.append(b)
        return Solution.result[n]


s = Solution()
print(s.Fibonacci(30))


