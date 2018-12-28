package LintCode;


/**
 * 5. 第k大元素
 * @description 在数组中找到第k大的元素, 要求时间复杂度为O(n),空间复杂度为O(1)
 * @href https://www.lintcode.com/problem/kth-largest-element/description
 * @date: 2018-12-27
 */
public class Solution5 {

    /**
     * 可参考快速选择实现
     * 参考: https://zh.wikipedia.org/wiki/快速选择
     * @param n: An integer
     * @param nums: An array
     * @return: the Kth largest element
     */
    public static int kthLargestElement(int n, int[] nums) {
        return quickSelect(nums, 0, nums.length-1, nums.length - n);
    }

    public static int quickSelect(int[] arr, int head, int tail, int n) {
        if (head >= tail || arr == null || arr.length <= 1)
            return arr[tail];
        int i=head, j=tail, p=arr[(head + tail) / 2];
        while (i <= j) {
            while (arr[i] < p) {
                ++i;
            }
            while (arr[j] > p) {
                --j;
            }
            if (i < j) {
                int t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
                --j;
                ++i;
            } else if(i == j) {
                ++i;
            }
        }
        return n <= j ? quickSelect(arr, head, j, n) : quickSelect(arr, j+1, tail, n);
    }

    public static void main(String[] args) {
//        int[] arr = new int[]{1, 4, 8, 2, 55, 3, 4, 8, 6, 4, 0, 11, 34, 90, 23, 54, 77, 9, 2, 9, 4, 10};
        int[] arr = new int[]{1, 3,4,2};
        System.out.println(kthLargestElement(1, arr));

    }



}
