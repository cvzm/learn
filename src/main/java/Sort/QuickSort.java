package Sort;

import java.util.Arrays;

public class QuickSort {

    /**
     * 快速排序
     * 参考: https://zh.wikipedia.org/wiki/快速排序
     * @param arr
     * @param head
     * @param tail
     */
    public static void quickSort(int[] arr, int head, int tail) {
        if (head >= tail || arr == null || arr.length <= 1)
            return;
        int i=head, j=tail, pivot=arr[(head+tail)/2];
        while (i <= j) {
            while (arr[i] < pivot) {
                ++i;
            }
            while (arr[j] > pivot) {
                --j;
            }
            if (i < j) {
                int t = arr[i];
                arr[i] = arr[j];
                arr[j] = t;
                --j;
            }
            ++i;
        }
        quickSort(arr, head, j);
        quickSort(arr, i, tail);
    }

    public static void main(String[] args) {
        int[] arr = new int[]{1, 4, 8, 2, 55, 3, 4, 8, 6, 4, 0, 11, 34, 90, 23, 54, 77, 9, 2, 9, 4, 10};
        System.out.println(Arrays.toString(arr));
        quickSort(arr, 0, arr.length - 1);
        System.out.println(Arrays.toString(arr));

    }

}
