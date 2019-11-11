# -*- coding:utf-8 -*-
"""
题目描述
    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

    @href https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Print(self, pRoot):
        if not pRoot:
            return []
        res = []
        curNodes = [pRoot]
        while curNodes:
            nextNodes = []
            values = []
            for node in curNodes:
                values.append(node.val)
                if node.left:
                    nextNodes.append(node.left)
                if node.right:
                    nextNodes.append(node.right)
            curNodes = nextNodes
            res.append(values)
        return res


s = Solution()
print("ok")

