package LintCode;


import java.util.Arrays;
import java.util.HashMap;

/**
 * 56. 两数之和
 * @description 给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。
 * 你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围
 * @href https://www.lintcode.com/problem/two-sum/description
 * @date: 2019-1-15
 */
public class Solution56 {


    /**
     * 逻辑转换，求和亦是求差。 求证numbers存在 target - numbers[i] 的数即可。 可采用Map实现
     * @param numbers: An array of Integer
     * @param target: target = numbers[index1] + numbers[index2]
     * @return: [index1, index2] (index1 < index2)
     */
    public static int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < numbers.length; i++) {
            if (map.get(numbers[i]) != null) {
                return new int[]{map.get(numbers[i]), i};
            }
            map.put(target - numbers[i], i);
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum(new int[]{2,7,11,15}, 9)));
    }



}


