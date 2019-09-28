# -*- coding:utf-8 -*-
"""
题目描述
    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
    其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。
    不能使用除法。

    @href https://www.nowcoder.com/practice/94a4d381a68b47b7a8bed86f2975db46
"""
class Solution:

    def multiply(self, A):
        if not A or len(A) < 2:
            return []
        # 当前乘积
        current = 1
        # res
        B = [current]
        for i in range(1, len(A)):
            current *= A[i-1]
            B.append(current)

        current = 1
        for i in range(len(A)-2, -1, -1):
            current *= A[i+1]
            B[i] *= current

        return B

s = Solution()
print(s.multiply([1,2,3,4,5]))
# 24,24,12.4.1
print("ok")
