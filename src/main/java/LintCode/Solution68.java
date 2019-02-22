package LintCode;


import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * 68. 二叉树的后序遍历
 * @description 给出一棵二叉树，返回其节点值的后序遍历。  * 使用非递归实现
 * @href https://www.lintcode.com/problem/binary-tree-postorder-traversal/description
 * @date: 2019-02-21
 */
public class Solution68 {

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
     * @return: Postorder in ArrayList which contains node values.
     */
    public static List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> list = new LinkedList<>();
        if (root == null)
            return list;
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while (!stack.empty()) {
            TreeNode node = stack.pop();
            list.add(0, node.val);
            if (node.left != null) stack.push(node.left);
            if (node.right != null) stack.push(node.right);
        }
        return list;
    }


    public static void main(String[] args) {
        TreeNode node = new TreeNode(1);
        node.left = new TreeNode(2);
        node.right = new TreeNode(3);
        node.left.left = new TreeNode(4);
        postorderTraversal(node);
    }







}

