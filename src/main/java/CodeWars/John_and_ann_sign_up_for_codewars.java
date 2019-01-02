package CodeWars;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @description: 约翰与安加入了Codewars
 * @author: C.v.
 * @href https://www.codewars.com/kata/john-and-ann-sign-up-for-codewars
 * @date: 2019-1-2
 */
public class John_and_ann_sign_up_for_codewars {

    /**
     * 记录John每天的值
     */
    private static List<Long> John = new ArrayList<>();
    /**
     * 记录Ann每天的值
     */
    private static List<Long> Ann = new ArrayList<>();

    /**
     * 初始化第一天值
     */
    static {
       John.add(0L);
       Ann.add(1L);
    }

    /**
     * 推算指定天的值
     * @param n
     * @return
     */
    private static void compute(long n) {
        if (John.size() > n)
            return;
        int startDay = John.size() - 1;
        for (int i = startDay + 1; i < n; i++) {
            John.add(i - Ann.get(John.get(i-1).intValue()));
            Ann.add(i - John.get(Ann.get(i-1).intValue()));
        }
    }

    /**
     * 截取至n天的集合
     * @param temp
     * @param n
     * @return
     */
    private static List<Long> dirFetch(List<Long> temp, long n) {
        compute(n);
        return temp.subList(0, (int)n);
    }

    /**
     * 计算至n天的值的和
     * @param temp
     * @param n
     * @return
     */
    private static long sum(List<Long> temp, long n) {
        return dirFetch(temp, n).stream().mapToLong(l -> l).sum();
    }

    /**
     * John至n天的结果集
     * @param n
     * @return
     */
    public static List<Long> john(long n) {
        return dirFetch(John, n);
    }

    /**
     * Ann至n天的结果集
     * @param n
     * @return
     */
    public static List<Long> ann(long n) {
        return dirFetch(Ann, n);
    }

    /**
     * 计算John至n天的值的和
     * @param n
     * @return
     */
    public static long sumJohn(long n) {
        return sum(John, n);
    }

    /**
     * 计算Ann至n天的值的和
     * @param n
     * @return
     */
    public static long sumAnn(long n) {
        return sum(Ann, n);
    }

    public static void main (String[] args) {
        System.out.println(Arrays.toString(john(100).toArray()));
        System.out.println(sumJohn(100));
    }


}
