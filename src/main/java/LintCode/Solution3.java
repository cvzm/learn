package LintCode;


/**
 * 2. 统计数字
 * @description 计算数字k在0到n中的出现的次数，k可能是0~9的一个值
 * @href https://www.lintcode.com/problem/digit-counts/description
 * @date: 2018-12-25
 */
public class Solution3 {

    /** 可以根据连续数的规律来简化算法, 统计每一位上k出现的次数, 需要主要K=0的情况。
     * @param k: An integer
     * @param n: An integer
     * @return: An integer denote the count of digit k in 1..n
     */
    public static int digitCounts(int k, int n) {
        if (k<0 || k>9)
            return -1;
        int count = 0;
        int temp = n;
        int multiple = 1;
        while (temp != 0) {
            int tail = temp - temp/10*10;
            count += temp/10 * multiple;
            if (tail > k) {
                count += multiple;
            } else if (tail == k) {
                count += n - temp * multiple + 1;
            }
            if (k == 0)
                count -= multiple;
            multiple *= 10;
            temp /= 10;
        }
        return k==0 ? ++count : count;
    }

    public static void main(String[] args) {
        System.out.println(digitCounts(1, 6158));
        System.out.println(digitCounts(0, 6158));

    }




}
