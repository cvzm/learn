# -*- coding:utf-8 -*-

"""
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
    @href https://www.nowcoder.com/practice/947f6eb80d944a84850b0538bf0ec3a5
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.last = None

    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            print("node is none")
            return None
        if pRootOfTree.left is None and pRootOfTree.right is None:
            self.last = pRootOfTree
            print("设置last=", pRootOfTree.val)
            return pRootOfTree

        print("递归", pRootOfTree.val, "left")
        pLeft = self.Convert(pRootOfTree.left)
        print("递归", pRootOfTree.val, "left 完成")
        if pLeft:
            print("将", self.last.val, "right 设置为", pRootOfTree.val)
            self.last.right = pRootOfTree
            print("将", pRootOfTree.val, "left 设置为", self.last.val)
            pRootOfTree.left = self.last

        print("设置last=", pRootOfTree.val)
        self.last = pRootOfTree

        print("递归", pRootOfTree.val, "right")
        pRight = self.Convert(pRootOfTree.right)
        print("递归", pRootOfTree.val, "right 完成")
        if pRight:
            print("将", pRight.val, "left 设置为", pRootOfTree.val)
            pRight.left = pRootOfTree
            print("将", pRootOfTree.val, "right 设置为", pRight.val)
            pRootOfTree.right = pRight

        print("返回", str(pLeft.val) + " pLeft" if pLeft else str(pRootOfTree.val) + " root")
        return pLeft if pLeft else pRootOfTree




s = Solution()
# 用例1
# r1 = TreeNode(5)
# r1.left = TreeNode(3)
# r1.left.left = TreeNode(2)
# r1.left.right = TreeNode(4)
# r1.right = TreeNode(6)
# print("res:", "2,3,4,5,6")

# 用例2
r1 = TreeNode(5)
r1.left = TreeNode(4)
r1.left.left = TreeNode(3)
r1.left.left.left = TreeNode(2)
r1.left.left.left.left = TreeNode(1)

p = s.Convert(r1)
print(p)

