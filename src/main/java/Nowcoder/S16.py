# -*- coding:utf-8 -*-

# 题目描述
# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
#  @href https://www.nowcoder.com/practice/d8b6b4358f774294a89de2a6ac4d9337


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        res = ListNode(0)
        old = res
        # 指针跳出
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                val = pHead1.val
                pHead1 = pHead1.next
            else:
                val = pHead2.val
                pHead2 = pHead2.next
            old.next = ListNode(val)
            old = old.next
        old.next = pHead2 if pHead1 is None else pHead1
        return res.next


s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
print(s.Merge(l, l))


