# -*- coding:utf-8 -*-

"""
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
    @href https://www.nowcoder.com/practice/f836b2c43afc4b35ad6adc41ec941dba
"""


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return pHead

        # 向后copy每个next
        bNode = pHead
        while bNode:
            node = RandomListNode(bNode.label)
            node.next = bNode.next
            bNode.next = node
            bNode = node.next

        # 处理 random 指针
        bNode = pHead
        while bNode:
            node = bNode.next
            if bNode.random:
                node.random = bNode.random.next
            bNode = node.next

        # 取偶数位元素
        bNode = pHead
        pHead = pHead.next
        while bNode.next:
            node = bNode.next
            bNode.next = node.next
            bNode = node

        return pHead


s = Solution()
r1 = RandomListNode(1)
r1.next = RandomListNode(2)
r1.next.next = RandomListNode(3)
res = s.Clone(r1)
print(res)
