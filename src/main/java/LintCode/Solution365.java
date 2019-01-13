package LintCode;



/**
 * 365. 二进制中有多少个1
 * @description 计算在一个 32 位的整数的二进制表示中有多少个 1.   * If the integer is n bits with m 1 bits. Can you do it in O(m) time?
 * @href https://www.lintcode.com/problem/count-1-in-binary/description
 * @date: 2019-1-12
 */
public class Solution365 {

    /**
     * 通过按位与实现，每次num & num-1 可统计出1减少的次数
     * @param num: An integer
     * @return: An integer
     */
    public static int countOnes(int num) {
        int count = 0;
        while (num != 0) {
            num = num & (num - 1);
            count++;
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(countOnes(32));
    }



}


