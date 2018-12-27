package LintCode;


import java.util.ArrayList;
import java.util.List;

/**
 * 4. 丑数 II
 * @description 设计一个算法，找出只含素因子2，3，5 的第 n 小的数。
 * @href https://www.lintcode.com/problem/ugly-number-ii/description
 * @date: 2018-12-27
 */
public class Solution4 {

    /**
     * 需要掌握 丑数 的基本知识。 丑数通过乘2,3,5得出之后的丑数
     * @param n: An integer
     * @return: the nth prime number as description.
     */
    public static int nthUglyNumber(int n) {
        List<Integer> res = new ArrayList<>();
        res.add(1);
        int s2=0, s3=0, s5=0;
        for (int i=1; i<n; i++) {
            int t2 = res.get(s2) * 2;
            int t3 = res.get(s3) * 3;
            int t5 = res.get(s5) * 5;
            int min = Math.min(Math.min(t2, t3), t5);
            if (min == t2)
                s2++;
            if (min == t3)
                s3++;
            if (min == t5)
                s5++;
            res.add(min);
        }
        return res.get(n-1);
    }

    public static void main(String[] args) {
        System.out.println(nthUglyNumber(41));

    }



}
