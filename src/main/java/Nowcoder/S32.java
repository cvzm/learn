package Nowcoder;


import java.util.*;
import java.util.stream.Collectors;

/**
 * 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
 *     @href https://www.nowcoder.com/practice/8fecd3f8ba334add803bf2a06af1b993
 */
public class S32 {

    public static String PrintMinNumber(int[] numbers) {
        return Arrays.stream(numbers)
                .mapToObj(Objects::toString)
                .sorted((x, y) -> (x + y).compareTo(y + x))
                .collect(Collectors.joining());
    }

    public static void main(String[] args) {
        PrintMinNumber(new int[]{3, 32, 321});
        PrintMinNumber(new int[]{5, 4, 1, 7});
    }

}
