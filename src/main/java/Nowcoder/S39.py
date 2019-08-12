# -*- coding:utf-8 -*-
"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

    注： 平衡二叉树，它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

    @href https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.TreeDepth(pRoot)
        return self.flag

    def TreeDepth(self, pRoot):
        if not pRoot or self.flag is False:
            return 0
        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        if abs(left - right) > 1:
            self.flag = False
        return 1 + (left if left > right else right)


s = Solution()
t = TreeNode(1)
t.left = TreeNode(11)
t.right = TreeNode(12)
t.left.left = TreeNode(111)
t.left.right = TreeNode(112)
# t.right.left = TreeNode(121)
# t.right.right = TreeNode(122)
print(s.IsBalanced_Solution(t))

