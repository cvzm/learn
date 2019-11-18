# -*- coding:utf-8 -*-
"""
题目描述
    给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。

    @href https://www.nowcoder.com/practice/ef068f602dde4d28aab2b210e859150a
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    res = 0

    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return
        left = self.KthNode(pRoot.left, k)
        self.res += 1
        if self.res == k:
            return pRoot
        right = self.KthNode(pRoot.right, k)
        if left:
            return left
        elif right:
            return right


a = TreeNode(8)
a.left = TreeNode(6)
a.right = TreeNode(10)
a.left.left = TreeNode(5)
a.left.right = TreeNode(7)
a.right.left = TreeNode(9)
a.right.right = TreeNode(11)
# print(Solution().KthNode(a, 1))
# print(Solution().KthNode(a, 2))
# print(Solution().KthNode(a, 3))
# print(Solution().KthNode(a, 4))
print(Solution().KthNode(a, 5))
print("ok")

