package CodeWars;

import java.util.stream.LongStream;

/**
 * @description: 整数：创意1
 * @author: C.v.
 * @href https://www.codewars.com/kata/integers-recreation-one
 * @date: 2019-1-2
 */
public class Integers_recreation_one {

    public static String listSquared(long m, long n) {
        StringBuilder res = new StringBuilder("[");
        for (long i=m; i<=n; i++) {
            final long temp = i;
            //求因数平方和
            long sum = LongStream.range(1, i+1)
                    .filter(t -> temp % t == 0)
                    .map(s -> s*s).sum();
            //判断是否为平方数
            double d = Math.sqrt(sum);
            if (d - (int)d > 0)
                continue;
            res.append("[").append(i).append(", ").append(sum).append("]").append(", ");
        }
        if (res.length() != 1)
            res.deleteCharAt(res.length()-1).deleteCharAt(res.length()-1);
        res.append("]");
        return res.toString();
    }

    public static void main (String[] args) {
        System.out.println(listSquared(1,250));
        System.out.println(listSquared(250,500));
    }
}
