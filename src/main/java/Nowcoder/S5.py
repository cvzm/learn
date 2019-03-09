# -*- coding:utf-8 -*-


# 题目描述
#  用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#  @href https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6
class Solution:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


sl = Solution()
sl.push(99)
sl.push(100)
print(sl.pop())
sl.push(111)
print(sl.pop())
