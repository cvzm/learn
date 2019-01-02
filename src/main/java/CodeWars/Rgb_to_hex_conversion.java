package CodeWars;

import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * @description: RGB转换为十六进制
 * @author: C.v.
 * @href https://www.codewars.com/kata/rgb-to-hex-conversion/
 * @date: 2019-1-1
 */
public class Rgb_to_hex_conversion {

    public static String rgb(int r, int g, int b) {
        return Stream.of(r, g, b)
                .map(i -> Integer.toHexString(i < 0 ? 0 : i > 255 ? 255 : i))
                .collect(Collectors.joining());
    }

    public static void main (String[] args) {
        System.out.println(rgb(225, 1, 123));
    }
}
