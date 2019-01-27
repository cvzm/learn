package LintCode;


/**
 * 141. x的平方根
 * @description 实现 int sqrt(int x) 函数，计算并返回 x 的平方根。返回对x开根号后向下取整的结果
 * @href https://www.lintcode.com/problem/sqrtx/description
 * @date: 2018-12-24
 */
public class Solution141 {

    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public static int sqrt(int x) {
        if (x < 2)
            return x;
        int start = 1, end = x;
        while (start + 1 < end) {
            int m = start + (end - start) / 2;
            if ((long) m * m <= x) {
                start = m;
            } else {
                end = m;
            }
        }
        return start;
    }

    public static void main(String[] args) {
        System.out.println(sqrt(2147483647));
    }






}
