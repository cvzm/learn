package CodeWars;

import java.util.Arrays;

/**
 * @description: 数字的重量
 * @author: C.v.
 * @date: 2018-12-10
 */
public class WeightSort {
    public static String orderWeight(String strng) {
        if (strng == null || strng.trim().length() == 0) return "";
//        String[] a = strng.trim().replaceAll("[ ]{2,}", " ").split(" ");
        String[] a = strng.trim().split(" ");
        Arrays.sort(a, (o1, o2) -> {
            if (o1.isEmpty() || o2.isEmpty())
                return 0;
            int[] sum = new int[]{0,0};
            o1.chars()
                    .filter(i -> i != 48)
                    .forEach(i -> sum[0] += i-48);
            o2.chars()
                    .filter(i -> i != 48)
                    .forEach(i -> sum[1] += i-48);
            if (sum[0] == sum[1]) {
                return WeightSort.sort(o1, o2) ? 1 : -1;
            }
            return sum[0] > sum[1] ? 1 : -1;
        });

        return WeightSort.toString(a);
    }

    /**
     * 字符串数组转字符串
     */
    private static String toString(String[] a) {
        if (a == null || a.length == 0)
            return "";
        int iMax = a.length - 1;

        StringBuilder b = new StringBuilder();
        for (int i = 0; ; i++) {
            if (a[i].isEmpty())
                continue;
            b.append(String.valueOf(a[i]));
            if (i == iMax)
                return b.toString();
            b.append(" ");
        }
    }

    /**
     * 字符串大小比较
     */
    private static boolean sort(String o1, String o2) {

        int length = o1.length() > o2.length() ? o2.length() : o1.length();
        for (int i=0; i<length; i++) {
            if (o1.codePointAt(i) != o2.codePointAt(i))
                return o1.codePointAt(i) > o2.codePointAt(i);
        }
        return false;
    }

    public static void main (String[] args) {
        System.out.println(WeightSort.orderWeight("  100 10  "));
        System.out.println(WeightSort.orderWeight("  2000 10003 1234000 44444444 9999 11 11 22 123  "));
        System.out.println(WeightSort.orderWeight("     103 123  4444 99 2000 180 90 "));
    }

}
