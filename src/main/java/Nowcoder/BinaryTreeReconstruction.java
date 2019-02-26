package Nowcoder;


import java.util.Arrays;

/**
 * 题目描述
 * 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
 * 例如输入前序遍历序列（1，2，4, 7, 3，5, 6，8}和中序遍历序列（4，7, 2，1, 5, 3, 8，6），则重建二叉树并返回。
 * @href https://www.nowcoder.com/practice/8a19cbe657394eeaac2f6ea9b0f6fcf6
 */
public class BinaryTreeReconstruction {

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

    public  static TreeNode reConstructBinaryTree(int[] pre, int[] in) {
        if (pre.length == 0 || in.length == 0)
            return null;

        TreeNode tree = new TreeNode(pre[0]);
        for (int i = 0; i < pre.length; i++) {
            if (in[i] == pre[0]) {
                tree.left = reConstructBinaryTree(Arrays.copyOfRange(pre, 1, i + 1), Arrays.copyOfRange(in, 0, i));
                tree.right = reConstructBinaryTree(Arrays.copyOfRange(pre, i + 1, pre.length), Arrays.copyOfRange(in, i + 1, in.length));
                break;
            }
        }
        return tree;
    }



    public static void main(String[] args) {
        int preorder[] ={ 1, 2, 4, 5, 3, 6, 7  };
        int inorder[] =  {  4, 2, 5, 1, 6, 3, 7 };

        TreeNode treeNode = reConstructBinaryTree(preorder, inorder);
        System.out.println(treeNode.val);
    }


}
