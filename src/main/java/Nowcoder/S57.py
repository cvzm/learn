# -*- coding:utf-8 -*-
"""
题目描述
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

    @href https://www.nowcoder.com/practice/9023a0c988684a53960365b889ceaf5e
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    # 节点存在右子树，下个节点则是右子树的最左节点
    # 节点不存在右子树：
    #       1. 节点是父节点的左节点，则下个节点是父节点
    #       2. 节点是父节点的右节点，则向上遍历，重复1的判断


    def GetNext(self, pNode):
        # 二叉树为空
        if not pNode:
            return None
        # 有右节点，找右节点的最左节点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        # 没有右边节点
        while pNode.next:
            if pNode == pNode.next.left:
                return pNode.next
            pNode = pNode.next
        return None


s = Solution()
print("ok")

