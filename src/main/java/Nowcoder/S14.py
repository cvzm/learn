# -*- coding:utf-8 -*-

# 题目描述
# 输入一个链表，输出该链表中倒数第k个结点。
#  @href https://www.nowcoder.com/practice/529d3ae5a407492994ad2a246518148a


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 时间O(n), 空间O(n)
    def FindKthToTail(self, head, k):
        if not head or k == 0:
            return None
        res = []
        next = head
        while next:
            res.append(next)
            next = next.next
        if k > len(res):
            return None
        return res[len(res) - k]

    # 时间O(2n), 空间O(1)
    # 将倒序转为正序
    def FindKthToTail2(self, head, k):
        if not head or k == 0:
            return None
        count = 0
        next = head
        while next:
            next = next.next
            count = count + 1
        if k > count:
            return None
        count = count - k
        next = head
        while count > 0:
            next = next.next
            count = count - 1
        return next



s = Solution()
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
print(s.FindKthToTail2(l, 5))




