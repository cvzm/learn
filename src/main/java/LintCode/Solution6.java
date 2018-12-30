package LintCode;


import java.util.Arrays;

/**
 * 6. 合并排序数组 II
 * @description 合并两个排序的整数数组A和B变成一个新的数组。
 * @href https://www.lintcode.com/problem/merge-two-sorted-arrays/description
 * @date: 2018-12-30
 */
public class Solution6 {

    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public static int[] mergeSortedArray(int[] A, int[] B) {
        int sum = A.length + B.length;
        int[] c = new int[sum];
        int a=0, b=0;
        for (int i=0; i<sum; i++) {
            if (a == A.length) {
                c[i] = B[b++];
                continue;
            } else if (b == B.length) {
                c[i] = A[a++];
                continue;
            }
            if (A[a] < B[b]) {
                c[i] = A[a++];
            } else if(B[b] < A[a]) {
                c[i] = B[b++];
            } else {
                c[i++] = A[a++];
                c[i] = B[b++];
            }
        }
        return c;
    }

    public static void main(String[] args) {
        int[] a = new int[]{1, 2, 3, 5, 6, 8};
        int[] b = new int[]{1, 3, 4, 10};
        System.out.println(Arrays.toString(mergeSortedArray(a, b)));

    }



}
