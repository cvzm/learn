package LintCode;



/**
 * 8. 旋转字符串
 * @description 给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)   *在数组上原地旋转，使用O(1)的额外空间
 * @href https://www.lintcode.com/problem/rotate-string/description
 * @date: 2019-1-7
 */
public class Solution8 {

    /**
     * @param str: An array of char
     * @param offset: An integer
     * @return: nothing
     */
    public static void rotateString(char[] str, int offset) {
        if (str == null || str.length == 0)
            return;
        int cutting = offset % str.length;
        if (cutting == 0)
            return;
        reverse(str, 0, str.length - 1 - cutting);
        reverse(str, str.length - cutting, str.length - 1);
        reverse(str, 0, str.length - 1);
    }

    private static void reverse(char[] str, int start, int end) {
        for (int i=start, j=end; i<j; i++, j--) {
            char temp = str[i];
            str[i] = str[j];
            str[j] = temp;
        }
    }

    public static void main(String[] args) {
        char[] c = {'a','b','c','d','e','f','g'};
        rotateString(c, 3);
    }

}


