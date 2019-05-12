# -*- coding:utf-8 -*-

"""
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
    @href https://www.nowcoder.com/practice/a861533d45854474ac791d90e447bafd


本题需要注意的是， 二叉搜索数， 而不是普通的二叉树
有关二叉搜索树可参考 https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
它的特性有
    1. 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
    2. 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
    3. 任意节点的左、右子树也分别为二叉查找树；
    4. 没有键值相等的节点。
"""
class Solution:

    def VerifySquenceOfBST(self, sequence):
        size = len(sequence)
        if size == 0:
            return False
        if size < 3:
            return True

        root = sequence[-1]
        # 判断找到左右节点分界值
        i = 0
        for i in range(size):
            if sequence[i] > root:
                break

        # 校验右节点是否均大于根节点。
        j = i
        for j in range(i, size):
            if sequence[j] < root:
                return False

        # 校验左子树是否满足搜索树
        left = self.VerifySquenceOfBST(sequence[0: i]) if i > 0 else True
        right = self.VerifySquenceOfBST(sequence[i: j]) if i < size - 1 else True

        return left and right




s = Solution()
l = [1, 2, 3, 4, 5]
print(s.VerifySquenceOfBST(l))

# 1 24  3 68 7 5

# 判断 是否 大于 最后个元素(根节点)  可以得知  左右的分界线
# 例如此处的 3， 同时 3 也是左树的根节点， 可以在次递归校验

