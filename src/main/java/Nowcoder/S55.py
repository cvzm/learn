# -*- coding:utf-8 -*-
"""
题目描述
    给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

    @href https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def EntryNodeOfLoop(self, pHead):
        # 判断下个节点是否出现过
        ids = []
        this_pHead = pHead

        while this_pHead.next:
            ids.append(this_pHead)
            if ids.__contains__(this_pHead.next):
                return this_pHead.next
            this_pHead = this_pHead.next

        return None


s = Solution()
a = [1,2]
print(a.__contains__(3))
print("ok")

