package LintCode;


import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

/**
 * 66. 二叉树的前序遍历
 * @description 给出一棵二叉树，返回其节点值的前序遍历。  * 使用非递归实现
 * @href https://www.lintcode.com/problem/binary-tree-preorder-traversal/description
 * @date: 2019-02-21
 */
public class Solution66 {

    /**
     * Definition of TreeNode:
     */
    public static class TreeNode {
        public int val;
        public TreeNode left, right;
        public TreeNode(int val) {
            this.val = val;
            this.left = this.right = null;
        }
    }

    /**
     * @param root: A Tree
     * @return: Preorder in ArrayList which contains node values.
     */
    public static List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        if (root == null)
            return list;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            list.add(node.val);
            if (node.right != null)
                stack.push(node.right);
            if (node.left != null)
                stack.push(node.left);
        }
        return list;
    }


    public static void main(String[] args) {
        TreeNode node = new TreeNode(1);
        node.left = new TreeNode(2);
        node.right = new TreeNode(3);
        node.left.left = new TreeNode(4);
        preorderTraversal(node);
    }







}

