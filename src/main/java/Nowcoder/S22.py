# -*- coding:utf-8 -*-

"""
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
    @href https://www.nowcoder.com/practice/7fe2212963db4790b57431d9ed259701
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 记录每层的父节点即可
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        # 结果集
        res = [root.val]
        # 节点集
        nodes = [root]
        for v in nodes:
            if v.left is not None:
                nodes.append(v.left)
                res.append(v.left.val)
            if v.right is not None:
                nodes.append(v.right)
                res.append(v.right.val)
        return res


s = Solution()
r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.left.left = TreeNode(3)
r1.left.right = TreeNode(33)
print(s.PrintFromTopToBottom(r1))
