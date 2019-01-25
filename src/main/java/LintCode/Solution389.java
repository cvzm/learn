package LintCode;


import java.util.HashSet;
import java.util.Set;

/**
 * 389. 判断数独是否合法
 * @description 请判定一个数独是否有效。
 * 该数独可能只填充了部分数字，其中缺少的数字用 . 表示。
 * @href https://www.lintcode.com/problem/valid-sudoku/description
 * @date: 2019-1-25
 */
public class Solution389 {

    /**
     * @param board: the board
     * @return: whether the Sudoku is valid
     */
    public static boolean isValidSudoku(char[][] board) {
        Set seen = new HashSet();
        int n = board.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                char num = board[i][j];
                if (num != '.') {
                    if (!seen.add(num + "r" + i) ||
                            !seen.add(num + "c" + j) ||
                            !seen.add(num + "b" + i/3 + "-" + j/3))
                        return false;

                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char[][] a = {
                {'.', 8, 7, 6, 5, 4, 3, 2, 1},
                {2, '.', '.', '.', '.', '.', '.', '.', '.'},
                {3, '.', '.', '.', '.', '.', '.', '.', '.'},
                {4, '.', '.', '.', '.', '.', '.', '.', '.'},
                {5, '.', '.', '.', '.', '.', '.', '.', '.'},
                {6, '.', '.', '.', '.', '.', '.', '.', '.'},
                {7, '.', '.', '.', '.', '.', '.', '.', '.'},
                {8, '.', 9, '.', '.', '.', '.', '.', '.'},
                {9, '.', '.', '.', '.', '.', '.', '.', '.'}
        };
        System.out.println(isValidSudoku(a));
    }



}


