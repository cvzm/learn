package LintCode;


/**
 * 514. 栅栏染色
 * @description 我们有一个栅栏，它有n个柱子，现在要给柱子染色，有k种颜色可以染。
 * 必须保证不存在超过2个相邻的柱子颜色相同，求有多少种染色方案。
 * @href https://www.lintcode.com/problem/paint-fence/description
 * @date: 2019-1-17
 */
public class Solution514 {

    /**
     * 题目可理解为， 不超过两个栅栏颜色一样。
     * 不要被试例影响，可将思路转变为 第1个栅栏有几种染色方案， 第2个栅栏有几种染色方案 ...
     * n1 = k
     * n2 = n1 * k
     * n3 = (n1 + n2) * (k-1)
     * n4 = (n2 + n3) * (k-1)
     * 推导过程:
     *      若排除相邻限制，则n3 = n2 * k,  n4 = n3 * k; 可以看出多个栅栏，方案就是上一个栅栏的方案乘k
     *      若加上限制， 则 对于n3而言， n2+n1的方案中，要排除n2和n1颜色的方案， 也就是说，n3的方案中不包括n2与n1相同颜色。
     *      即可推出 n3 = (n1 + n2) * (k-1)
     * @param n: non-negative integer, n posts
     * @param k: non-negative integer, k colors
     * @return: an integer, the total number of ways
     */
    public static int numWays(int n, int k) {
        if (n < 0 || k < 0)
            return 0;
        if (n == 1)
            return k;
        if (n == 2)
            return k * k;
        int before = k, now = before * k;
        for (int i=3; i<=n; i++) {
            int temp = now;
            now = (before + now) * (k-1);
            before = temp;
        }
        return now;
    }

    public static void main(String[] args) {
        System.out.println(numWays(6, 3));
    }




}


