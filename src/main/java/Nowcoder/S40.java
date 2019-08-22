package Nowcoder;

import org.junit.Test;

import java.util.Arrays;
import java.util.List;

/***
 * 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
 *     @href https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811
 */

public class S40 {

    //num1,num2分别为长度为1的数组。传出参数
    //将num1[0],num2[0]设置为返回结果
    public void FindNumsAppearOnce(int[] array, int num1[], int num2[]) {
        if (array == null || array.length <= 1) {
            num1[0] = num2[0] = 0;
            return;
        }
        int len = array.length, index = 0, sum = 0;
        for (int i = 0; i < len; i++) {
            sum ^= array[i];
        }
        for (index = 0; index < 32; index++) {
            if ((sum & (1 << index)) != 0) break;
        }
        for (int i = 0; i < len; i++) {
            if ((array[i] & (1 << index)) != 0) {

                num2[0] ^= array[i];
            } else {
                num1[0] ^= array[i];
            }
        }
    }

    @Test
    public void test() {
        int[] arr = {3, 3, 4, 4, 7, 5};
        int num1[] = {0};
        int num2[] = {0};

//        FindNumsAppearOnce(arr, num1, num2);
        FindNumsAppearOnce2(arr, num1, num2);
        System.out.println(num1[0]);
        System.out.println(num2[0]);

    }

    private void FindNumsAppearOnce2(int[] array, int num1[], int num2[]) {
        var sum = new int[]{0};
        Arrays.stream(array).forEach(i -> sum[0] ^= i);
        var index = 1;
        for (; index < 32; index++) {
            if ((sum[0] & (1 << index)) != 0)
                break;
        }
        var place  = 1 << index;
        Arrays.stream(array).forEach(i -> {
            if ((i & place) != 0)
                num1[0] ^= i;
            else
                num2[0] ^= i;
        });
    }


}