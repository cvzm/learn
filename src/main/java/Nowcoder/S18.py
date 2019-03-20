# -*- coding:utf-8 -*-

# 题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。
#  @href https://www.nowcoder.com/practice/564f4c26aa584921bc75623e48ca3011


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Mirror(self, root):
        if root is None:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root


s = Solution()
r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.left.left = TreeNode(22)
r1.left.right = TreeNode(23)
r1.right = TreeNode(3)
r1.right.right = TreeNode(33)

p = s.Mirror(r1)
print(p)

