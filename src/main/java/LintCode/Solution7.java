package LintCode;


import java.util.LinkedList;
import java.util.Queue;

/**
 * 7. 二叉树的序列化和反序列化
 * @description 设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。
 * 如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。
 * @href https://www.lintcode.com/problem/serialize-and-deserialize-binary-tree/description
 * @date: 2018-12-30
 */
public class Solution7 {

    /**
     * Definition of TreeNode:
     */
    static class TreeNode {
        int val;
        TreeNode left, right;
        TreeNode(int val) {
            this.val = val;
            this.left = this.right = null;
        }
    }

    /**
     * 拼接符
     */
    private static final String SPLICING = ",";

    /**
     * This method will be invoked first, you should design your own algorithm
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public static String serialize(TreeNode root) {
        if (root == null)
            return SPLICING;
        return root.val + SPLICING + serialize(root.left) + serialize(root.right);
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in
     * "serialize" method.
     */
    public static TreeNode deserialize(String data) {
        if (data == null || "".equals(data) || SPLICING.equals(data.charAt(0) + ""))
            return null;
        //使用队列更符合目前的场景, 如不使用队列，可以通过移动数组下标实现。
        Queue<TreeNode> queue = new LinkedList<>();
        for (String valStr : data.split(SPLICING)) {
            queue.offer("".equals(valStr) ? null : new TreeNode(Integer.parseInt(valStr)));
        }
        return build(queue);
    }

    /**
     * 构建实体
     * @param queue
     * @return
     */
    public static TreeNode build(Queue<TreeNode> queue) {
        TreeNode node = queue.poll();
        if (node == null)
            return null;
        node.left = build(queue);
        node.right = build(queue);
        return node;
    }

    public static void main(String[] args) {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.left = new TreeNode(4);
        root.left.right = new TreeNode(5);
        root.right.left = new TreeNode(6);
        root.right.right = new TreeNode(7);
        System.out.println(serialize(root));
        TreeNode treeNode = deserialize(serialize(root));
        System.out.println(serialize(treeNode));
    }



}

