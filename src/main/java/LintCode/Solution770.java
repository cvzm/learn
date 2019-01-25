package LintCode;


import java.util.Arrays;

/**
 * 770. 最大数和最小数
 * @description 给定一个矩阵，返回矩阵中的最大数和最小数
 * @href https://www.lintcode.com/problem/maximum-and-minimum/description
 * @date: 2019-1-25
 */
public class Solution770 {

    /**
     * @param matrix: an input matrix
     * @return: nums[0]: the maximum,nums[1]: the minimum
     */
    public static int[] maxAndMin(int[][] matrix) {
        if (matrix == null || matrix.length == 0)
            return new int[]{};
        int min = matrix[0][0], max = min;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] < min) {
                    min = matrix[i][j];
                } else if (matrix[i][j] > max) {
                    max = matrix[i][j];
                }
            }
        }
        return new int[]{max, min};
    }

    public static void main(String[] args) {
        int[][] a = {{1,2,3},{4,3,2},{6,4,4}};
        System.out.println(Arrays.toString(maxAndMin(a)));
    }



}


