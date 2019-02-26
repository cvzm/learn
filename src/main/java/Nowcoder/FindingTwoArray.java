package Nowcoder;


/**
 * 题目描述
 *
 * 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
 * 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 * @href https://www.nowcoder.com/practice/abc3fe2ce8e146608e868a70efebf62e
 */
public class FindingTwoArray {

    /**
     * 采用二分查找
     * @param target
     * @param array
     * @return
     */
    public static boolean Find(int target, int [][] array) {
        if (array.length == 0 || array[0].length == 0)
            return false;
        for (int i = 0; i < array.length; i++) {
            int j = array[i].length - 1;
            if (array[i][j] < target)
                continue;
            int start = 0, end = j;
            while (start <= end){
                int mid = start + (end - start) / 2;
                if (array[i][mid] > target)
                    end = mid - 1;
                else if (array[i][mid] < target)
                    start = mid + 1;
                else
                    return true;
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int array[][] = {
                {1,2,3,4,5},
                {6,7,8,9,10}
        };
        System.out.println(Find(7, array));
    }


}
