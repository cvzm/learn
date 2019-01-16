package LintCode;


/**
 * 515. 房屋染色
 * @description 这里有n个房子在一列直线上，现在我们需要给房屋染色，分别有红色蓝色和绿色。每个房屋染不同的颜色费用也不同，你需要设计一种染色方案使得相邻的房屋颜色不同，并且费用最小。
 * @href https://www.lintcode.com/problem/paint-house/description
 * @date: 2019-1-16
 */
public class Solution515 {

    /**
     * 使用动态规划求解, 用矩阵存储之前的最小解
     * @param costs: n x 3 cost matrix
     * @return: An integer, the minimum cost to paint all houses
     */
    public static int minCost(int[][] costs) {
        int n = costs.length;
        int[][] dp = new int[2][3];
        int old, now = 0;
        for (int i = 0; i < n; i++) {
            old = now;
            now = 1 - old;
            dp[now][0] = Math.min(dp[old][1], dp[old][2]) + costs[i][0];
            dp[now][1] = Math.min(dp[old][0], dp[old][2]) + costs[i][1];
            dp[now][2] = Math.min(dp[old][0], dp[old][1]) + costs[i][2];
        }
        return Math.min(dp[now][0], Math.min(dp[now][1], dp[now][2]));
    }

    public static void main(String[] args) {
        System.out.println(minCost(new int[][]{{14,2,11},{11,14,5},{14,3,10}}));
    }



}


