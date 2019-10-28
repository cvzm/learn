# -*- coding:utf-8 -*-
"""
题目描述
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

    @href https://www.nowcoder.com/practice/fc533c45b73a41b0b44ccba763f866ef
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplication(self, pHead):
        first = ListNode(-1)
        first.next = pHead
        last = first
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and val == pHead.val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next
        return first.next


s = Solution()
a = ListNode(1)
a.next = ListNode(1)
a.next.next = ListNode(1)
a.next.next.next = ListNode(1)
# a.next.next.next.next = ListNode(2)
res = s.deleteDuplication(a)
print("run ok")
while res:
    print(res.val)
    res = res.next
print("ok")

