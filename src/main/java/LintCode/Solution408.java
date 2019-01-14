package LintCode;



/**
 * 408. 二进制求和
 * @description 给定两个二进制字符串，返回他们的和（用二进制表示）。
 * @href https://www.lintcode.com/problem/add-binary/description
 * @date: 2019-1-13
 */
public class Solution408 {

//    /**
//     * 源逻辑
//     * @param a: a number
//     * @param b: a number
//     * @return: the result
//     */
//    public static String addBinary(String a, String b) {
//        StringBuilder res = new StringBuilder(a.length() >= b.length() ? a : b);
//        boolean carry = false;
//        for (int i = 1; i <= res.length(); i++) {
//            int ai = a.length() - i;
//            int bi = b.length() - i;
//            int ri = res.length() - i;
//            boolean temp = false;
//            if (ai >= 0 && bi >= 0) {
//                if (a.charAt(ai) == b.charAt(bi)) {
//                    if (res.charAt(ri) != '0') {
//                        res.setCharAt(ri, '0');
//                        temp = true;
//                    }
//                } else {
//                    if (res.charAt(ri) != '1') {
//                        res.setCharAt(ri, '1');
//                    }
//                }
//            }
//            if (carry) {
//                if (res.charAt(ri) != '0') {
//                    res.setCharAt(ri, '0');
//                    temp = true;
//                } else {
//                    res.setCharAt(ri, '1');
//                }
//            }
//            carry = temp;
//        }
//        return carry ? "1" + res.toString() : res.toString();
//    }

    /**
     * 九章，减少没必要的判断
     * @param a a number
     * @param b a number
     * @return the result
     */
    public static String addBinary(String a, String b) {
        StringBuilder ans = new StringBuilder();
        int carry = 0;
        for (int i = a.length() - 1, j = b.length() - 1; i >= 0 || j >= 0; i--, j--) {
            int sum = carry;
            sum += (i >= 0) ? a.charAt(i) - '0' : 0;
            sum += (j >= 0) ? b.charAt(j) - '0' : 0;
            ans.insert(0,sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) {
            ans.insert(0, carry);
        }
        return ans.toString();
    }

    public static void main(String[] args) {
        System.out.println(addBinary("0", "0"));
        System.out.println(addBinary("11", "1"));
        System.out.println(addBinary("110", "111"));

    }



}


