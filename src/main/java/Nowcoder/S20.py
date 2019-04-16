# -*- coding:utf-8 -*-

"""
题目描述
    定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
    @href https://www.nowcoder.com/practice/4c776177d2c04c2494f2555c9fcc1e49
"""


class Solution:

    stack, assist = [], []

    def push(self, node):
        self.assist.append(node if len(self.assist) == 0 or node < self.assist[-1] else self.assist[-1])
        self.stack.append(node)

    def pop(self):
        self.assist.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.assist[-1]


s = Solution()
s.push(3)
print(s.min())





