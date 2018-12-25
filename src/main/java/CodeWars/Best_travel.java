package CodeWars;


import java.util.List;

/**
 * @description: 最佳旅程
 * @href https://www.codewars.com/kata/best-travel
 * @author: C.v.
 * @date: 2018-12-12
 */
public class Best_travel {

    /**
     * 该问题本质上就是 求数组的最大组合值(同时满足该数不超过t, 并且最多使用k个数(不能重复))
     * 解决方式：
     *      1.动态规划， t=Onk       ✖
     * @param t 最大数
     * @param k 最多组合数
     * @param ls 数组
     * @return 能满足的最大组合数
     */
    public static Integer chooseBestSum(int t, int k, List<Integer> ls) {
        int result = -1;
        for (int i=0; i<ls.size(); i++) {
            if (ls.get(i) <= t) {
                if (k==1) {
                    result = Math.max(result, ls.get(i));
                } else {
                    Integer temp = chooseBestSum(t-ls.get(i),k-1, ls.subList(i+1, ls.size()));
                    if (temp!=null){
                        result=Math.max(result, ls.get(i)+temp);
                    }
                }
            }
        }

        if (result<0) return null;
        return result;
    }




}

