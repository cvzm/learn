package Nowcoder;


import org.junit.Test;
import org.junit.runner.RunWith;

import java.util.*;

/**
 * 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
 *     @href https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c
 */
public class S34 {

    public int FirstNotRepeatingChar(String str) {
        if (str == null || str.isBlank())
            return -1;
        var map = new LinkedHashMap<Integer, Integer>();
        str.chars().forEach(
                c -> map.put(c, map.getOrDefault(c, 0) + 1));
        var first = map.entrySet().stream().filter( m -> m.getValue() == 1).findFirst();
        return first.isPresent() ? first.get().getKey() : -1;
    }

    @Test
    public void junit() {
        var res = FirstNotRepeatingChar("google");
        assert res == 'l': "google";

        assert FirstNotRepeatingChar("aa") == -1 : "aa";
        assert FirstNotRepeatingChar("") == -1 : "";
        assert FirstNotRepeatingChar(null) == -1 : "null";
    }

}
