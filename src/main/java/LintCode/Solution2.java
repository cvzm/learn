package LintCode;


/**
 * 2. 尾部的零
 * @description 设计一个算法，计算出n阶乘中尾部零的个数
 * @href https://www.lintcode.com/problem/trailing-zeros/description
 * @date: 2018-12-24
 */
public class Solution2 {

    /**
     * 本题需要掌握 阶乘 的基本概念
     * 参考: https://zh.wikipedia.org/wiki/階乘
     * @param n: An integer
     * @return: An integer, denote the number of trailing zeros in n!
     */
    public static long trailingZeros(long n) {
        long r = 0;
        long baseNum = 5;
        while (n >= baseNum) {
            r += n/baseNum;
            baseNum *=5;
        }
        return r;
    }

    public static long trailingZeros2(long n) {
        long sum = 0;
        while (n != 0) {
            sum += n / 5;
            n /= 5;
        }
        return sum;
    }



    public static void main(String[] args) {
//        System.out.println(trailingZeros(7));
//        System.out.println(trailingZeros2(25));




    }




}
