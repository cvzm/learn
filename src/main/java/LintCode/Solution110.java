package LintCode;



/**
 * 110. 最小路径和
 * @description 给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。
 * @href https://www.lintcode.com/problem/minimum-path-sum/description
 * @date: 2019-1-24
 */
public class Solution110 {

    /**
     *
     * @param grid: a list of lists of integers
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public static int minPathSum(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] temp = new int[m][n];
        temp[0][0] = grid[0][0];
        for (int i = 1; i < m; i++) {
            temp[i][0] = temp[i-1][0] + grid[i][0];
        }
        for (int j = 1; j < n; j++) {
            temp[0][j] = temp[0][j-1] + grid[0][j];
        }
        for (int i=1; i<grid.length; i++) {
            for (int j=1; j<grid[i].length; j++) {
                temp[i][j] = Math.min(temp[i-1][j], temp[i][j-1]) + grid[i][j];
            }
        }
        return temp[m-1][n-1];
    }

    public static void main(String[] args) {
        int[][] a = {
                {1,3,1},
                {1,5,1},
                {4,2,1}
        };
        System.out.println(minPathSum(a));
    }





}


