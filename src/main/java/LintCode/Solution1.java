package LintCode;


/**
 * 1. A + B 问题  （不用+等运算符）
 * @description 给出两个整数 a 和 b , 求他们的和。
 * @href https://www.lintcode.com/problem/a-b-problem/description
 * @date: 2018-12-24
 */
public class Solution1 {

    /**
     * 本题需要掌握 位运算，按位与、或、异或等运算方法
     * 参考: https://blog.csdn.net/21aspnet/article/details/7387373
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b
     */
//    public static int aplusb(int a, int b) {
//        int c;
//        while ((a & b) != 0) {
//            c = (a & b) << 1;
//            b = a ^ b;
//            a = c;
//        }
//        return a | b;
//    }

    public static int aplusb(int a, int b) {
        int c;
        while (a != 0) {
            c = (a & b) << 1;
            b = a ^ b;
            a = c;
        }
        return b;
    }



    public static void main(String[] args) {
        System.out.println(aplusb(-5,7));
    }






}
