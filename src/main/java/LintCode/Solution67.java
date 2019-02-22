package LintCode;


import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * 67. 二叉树的中序遍历
 * @description 给出一棵二叉树，返回其中序遍历。  * 使用非递归实现
 * @href https://www.lintcode.com/problem/binary-tree-inorder-traversal/description
 * @date: 2019-02-21
 */
public class Solution67 {

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
     * @return: Inorder in ArrayList which contains node values.
     */
    public static List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> list = new LinkedList<>();
        if (root == null)
            return list;
        Stack<TreeNode> stack = new Stack<>();
        TreeNode node = root;
        while (node != null || ! stack.empty()) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            list.add(node.val);
            node = node.right;
        }
        return list;
    }


    public static void main(String[] args) {
        TreeNode node = new TreeNode(1);
        node.left = new TreeNode(2);
        node.right = new TreeNode(3);
        node.left.left = new TreeNode(4);
        inorderTraversal(node);
    }







}

