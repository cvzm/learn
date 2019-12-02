# -*- coding:utf-8 -*-
"""
    给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），
    每段绳子的长度记为k[0],k[1],...,k[m]。
    请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
    例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

    @href https://www.nowcoder.com/practice/57d85990ba5b440ab888fc72b0751bf8
"""


class Solution:

    def cutRope(self, number):
        if number < 2:
            return 0
        elif number == 2:
            return 1
        max_list = [0, 1, 2]
        for i in range(3, number+1):
            if i < number:
                max = i
            else:
                max = 0

            for j in range(1, i//2+1):
                tmp = max_list[j] * max_list[i-j]
                if tmp > max:
                    max = tmp
            max_list.append(max)

        return max_list[number]

