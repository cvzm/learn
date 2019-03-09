package Nowcoder;



/**
 * 题目描述
 * 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
 * @href https://www.nowcoder.com/practice/4060ac7e3e404ad1a894ef3e17650423?
 */
public class ReplaceBlankSpace {

    public static String replaceSpace(StringBuffer str) {
        char[] strChar = str.toString().toCharArray();
        StringBuffer res = new StringBuffer();
        for (char c : strChar) {
            res.append(c != ' ' ? c : "%20");
        }
        return res.toString();
    }

    public static void main(String[] args) {
        System.out.println(replaceSpace(new StringBuffer("asd asd  123 ")));
    }


}

