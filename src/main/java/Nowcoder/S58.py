# -*- coding:utf-8 -*-
"""
题目描述
    请实现一个函数，用来判断一颗二叉树是不是对称的。
    注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

    @href https://www.nowcoder.com/practice/ff05d44dfdb04e1d83bdbdab320efbcb
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        return self.traversal(pRoot.left, pRoot.right)

    def traversal(self, left, right):
        # 叶节点
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return self.traversal(left.left, right.right) and self.traversal(left.right, right.left)
        return False


s = Solution()
a = TreeLinkNode(1)
a.left = TreeLinkNode(2)
a.right = TreeLinkNode(2)
a.left.left = TreeLinkNode(3)
a.right.right = TreeLinkNode(3)
print(s.isSymmetrical(a))
print("ok")

