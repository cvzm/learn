package LintCode;


/**
 * 1218. 补数
 * @description 给定一个正整数，输出它的补数。补数是将原先数字的二进制表示按位取反，再换回十进制后得到的新数。
 * @href https://www.lintcode.com/problem/number-complement/description
 * @date: 2019-1-16
 */
public class Solution1218 {

    /**
     * 通过位移将num每一位取反即可。
     * @param num: an integer
     * @return: the complement number
     */
    public static int findComplement(int num) {
        int temp = 1;
        while (temp <= num && temp > 0) {
            num ^= temp;
            temp <<= 1;
        }
        return num;
    }

    public static void main(String[] args) {
        System.out.println(findComplement(5));
        System.out.println(findComplement(2147483646));
    }



}


