package LintCode;


/**
 * 92. 背包问题
 * @description 在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]
 * @href https://www.lintcode.com/problem/backpack/description
 * @date: 2019-02-11
 */
public class Solution92 {

    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public static int backPack(int m, int[] A) {
        int[] dp = new int[m + 1];
        for (int i = 0; i < A.length; i++) {
            for (int j = m; j >= A[i]; j--) {
                dp[j] = Math.max(dp[j], dp[j - A[i]] + A[i]);
                if (i == A.length - 1)
                    break;
            }
        }
        return dp[m];
    }


    public static void main(String[] args) {
        System.out.println(backPack(10, new int[]{5, 7, 2, 3}));
    }






}
