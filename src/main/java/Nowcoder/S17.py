# -*- coding:utf-8 -*-

# 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
#  @href https://www.nowcoder.com/practice/6e196c44c7004d15b1610b9afca8bd88


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 判断root2是否为root1的子数
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        if self.check(pRoot1, pRoot2):
            return True
        b = self.HasSubtree(pRoot1.left, pRoot2)
        if not b:
            b = self.HasSubtree(pRoot1.right, pRoot2)
        return b

    # 校验
    def check(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None or pRoot1.val != pRoot2.val:
            return False
        return self.check(pRoot1.left, pRoot2.left) and self.check(pRoot1.right, pRoot2.right)


s = Solution()
r1 = TreeNode(1)
r1.left = TreeNode(2)
r1.left.left = TreeNode(3)
r1.left.right = TreeNode(33)

r2 = TreeNode(2)
r2.left = TreeNode(3)
r2.right = TreeNode(33)

print(s.HasSubtree(r1, r2))


