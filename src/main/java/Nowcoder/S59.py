# -*- coding:utf-8 -*-
"""
题目描述
    请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
    第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。

    @href https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0
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
        isEvenLayer = False
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
            res.append(values if not isEvenLayer else values[::-1])
            isEvenLayer = not isEvenLayer
        return res


s = Solution()
print("ok")

