# -*- coding:utf-8 -*-
"""
输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
    @href https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return 1 + (left if left > right else right)


s = Solution()
t = TreeNode(1)
t.left = TreeNode(11)
t.right = TreeNode(12)
t.left.left = TreeNode(111)
t.left.right = TreeNode(112)
t.right.left = TreeNode(121)
t.right.right = TreeNode(122)
print(s.TreeDepth(t))