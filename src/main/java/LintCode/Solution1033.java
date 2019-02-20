package LintCode;


/**
 * 1033. BST中的最小差值
 * @description 给定一个确定根的二叉搜索树，返回树中任意两个不同节点的值的最小差。
 * @href https://www.lintcode.com/problem/minimum-difference-between-bst-nodes/description
 * @date: 2019-02-19
 */
public class Solution1033 {

    /**
     * Definition of TreeNode:
     */
    public class TreeNode {
        public int val;
        public TreeNode left, right;
        public TreeNode(int val) {
            this.val = val;
            this.left = this.right = null;
        }
    }

    private Integer res = Integer.MAX_VALUE, pre = null;

    /**
     * 中序遍历，找到差的最小值。
     * @param root: the root
     * @return: the minimum difference between the values of any two different nodes in the tree
     */
    public int minDiffInBST(TreeNode root) {
        if (root.left != null) {
            minDiffInBST(root.left);
        }
        if (pre != null) {
            res = Math.min(res, root.val - pre);
        }
        pre = root.val;
        if (root.right != null) {
            minDiffInBST(root.right);
        }
        return res;
    }


    public static void main(String[] args) {
        Solution1033 solution = new Solution1033();

    }






}
