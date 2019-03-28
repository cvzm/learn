package Other;

/**
 * @description 一个纯数字列表，有很多个偶数个数字，但只有一个奇数个数字，如何最高效找到它。
 * 例如 list[1,3,4,3,5,5,4,6,7,6,6,6,7] 例如这个,答案是1
 * @href
 * @date: 2019-03-28
 */
public class LookingForOddEven {

    public static void main(String[] args) {
        int[] list = {1,3,4,3,5,5,4,6,7,6,6,6,7};
        int res = 0;
        for (int i = 0; i < list.length; i++) {
            res ^= list[i];
        }
        System.out.println(res);
    }
}
