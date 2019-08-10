# -*- coding:utf-8 -*-
"""
输入两个链表，找出它们的第一个公共结点。
    @href https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindFirstCommonNode(self, pHead1, pHead2):
        size1 = self.getListNodeLen(pHead1)
        size2 = self.getListNodeLen(pHead2)

        # 给长链表去头
        if size1 != size2:
            d = abs(size1 - size2)
            if size1 > size2:
                pHead1 = self.getNextNth(pHead1, d)
            else:
                pHead2 = self.getNextNth(pHead2, d)

        for i in range(size1):
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next

    # 获取长度
    def getListNodeLen(self, node):
        size = 0
        while node is not None and node != node.next:
            size += 1
            node = node.next
        return size

    # 获取 下N个节点
    def getNextNth(self, node, nth):
        for i in range(nth):
            if node is None:
                return
            node = node.next
        return node


s = Solution()
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n2 = ListNode(1)
n2.next = ListNode(2)
n2.next.next = n.next.next
print(s.FindFirstCommonNode(n, n2).val)
