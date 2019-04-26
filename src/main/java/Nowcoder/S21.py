# -*- coding:utf-8 -*-

"""
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
    @href https://www.nowcoder.com/practice/d77d11405cc7470d82554cb392585106
"""


class Solution:

    # 用辅助栈实现
    def IsPopOrder2(self, pushV, popV):
        temp = []
        popI = 0
        for v in pushV:
            if v != popV[popI]:
                temp.append(v)
            else:
                popI += 1
        print(temp)
        for i in temp:
            if temp.pop() != popV[popI]:
                return False
            popI += 1

        return True

    # 简单递归实现
    def IsPopOrder(self, pushV, popV):
        # 长度
        size = len(pushV)
        if size == 0:
            return True
        # pop头 对应的 push下标，有三种情况。
        # 1. 0， 头头对应， index+1后递归判断
        # 2. size, 头对尾巴， 只有一种情况， 顺序递减，否则return False
        # 3. 0-size之间
        #       例如 size=5, index = 3
        #       则可能的情况为，34521， 35421
        #       由此可得， size-index 后的元素需要满足 push[index--] index递减，
        #                 若， index 和 size距离过长， 其中的数组也应递归该逻辑
        try:
            popOneI = pushV.index(popV[0])
        except:
            # 元素不存在
            return False

        if popOneI == 0:
            return self.IsPopOrder(pushV[1: size], popV[1: size])
        if popOneI == size - 1:
            i = size - 1
            for v in popV:
                pushI = pushV.index(v)
                if i != pushI:
                    return False
                i -= 1
            return True
        # 第三种情况。 计算差值 即pop头对应push下标至末尾的剩余元素数
        d = size - 1 - popOneI
        # 校验 popV[d] 后的元素 对应的push下标 是否顺序递减
        p = popOneI - 1
        for i in range(d + 1, size):
            pushI = pushV.index(popV[i])
            if p != pushI:
                return False
            p -= 1

        return self.IsPopOrder(pushV[popOneI: size], popV[0: d+1])



s = Solution()
# [4,5,6,7,1,2,3]
# [7,6,5,4,3,2,1]
print(s.IsPopOrder2([1,2,3,4,5,6,7], [4,5,6,7,3,2,1]))
# print(s.IsPopOrder2([1,2,3,4,5], [4,5,3,2,1]))
# print(s.IsPopOrder([1], [2]))


# 1  2  3  4  5  6  7
#
# 7654321
# 6754321
# 5674321
# 5764321
# 4567321
# 4576321
# 4765321
# 4675321
#


# pop 大值后就不能跳小值
# pop 小值后可以随意




