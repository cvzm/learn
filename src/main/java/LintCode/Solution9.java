package LintCode;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

/**
 * 9. Fizz Buzz 问题
 * @description 给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
 * 如果这个数被3整除，打印fizz.
 * 如果这个数被5整除，打印buzz.
 * 如果这个数能同时被3和5整除，打印fizz buzz.
 * * 你是否可以只用一个 if 来实现
 * @href https://www.lintcode.com/problem/fizz-buzz/description
 * @date: 2019-1-12
 */
public class Solution9 {

    /**
     * @param n: An integer
     * @return: A list of strings.
     */
    public static List<String> fizzBuzz(int n) {
        List<String> list = new ArrayList<>();
        IntStream.rangeClosed(1, n).forEach(i -> {
            String str = rule(i, 3, "fizz ") + rule(i, 5, "buzz ");
            if ("".equals(str)) {
                str += i;
            }
            list.add(str.trim());
        });
        return list;
    }

    private static String rule(int i, int d, String str) {
        return i % d == 0 ? str : "";
    }


    public static void main(String[] args) {
        System.out.println(fizzBuzz(15).toString());
    }

}


