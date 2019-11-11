# -*- coding:utf-8 -*-
"""
题目描述
    请实现两个函数，分别用来序列化和反序列化二叉树

    二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
    序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，
    序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

    二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。

    @href https://www.nowcoder.com/practice/cf7e25aa97c04cc1a68c8f040e71fb84
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    flag = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return str(root.val) + ',' + self.Serialize(root.left) + ',' + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.flag += 1
        l = s.split(',')
        # flag每次加1，从0开始，不能超过字符串长度，否则返回None
        if self.flag >= len(s):
            return None

        root = None
        # 新建一个树对象来反序列化字符串
        if l[self.flag] != '#':
            # 往树中存值,递归输入s没问题，因为l[self.flag]是不断往后取值的
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root


s = Solution()
print("ok")

