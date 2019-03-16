# -*- coding:utf-8 -*-

# 题目描述
# 输入一个链表，反转链表后，输出新链表的表头。
#  @href https://www.nowcoder.com/practice/75e878df47f24fdc9dc3e400ec6058ca


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 时间O(n), 空间O(n)
    def ReverseList(self, pHead):
        res = None
        while pHead:
            old = res
            res = ListNode(pHead.val)
            res.next = old
            pHead = pHead.next
        return res


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
print(s.ReverseList(l))



