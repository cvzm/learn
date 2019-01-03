package CodeWars;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * @description: 缩减方向
 * @author: C.v.
 * @href https://www.codewars.com/kata/directions-reduction
 * @date: 2019-1-2
 */
public class Directions_reduction {

    /**
     * 获取反向标示
     */
    private static String reverse(String direction) {
        switch (direction) {
            case "NORTH": return "SOUTH";
            case "SOUTH": return "NORTH";
            case "WEST": return "EAST";
            case "EAST": return "WEST";
            default: return "";
        }
    }

//    public static String[] dirReduc(String[] arr) {
//        String[] res= new String[arr.length];
//        int index = 0;
//        boolean isReverse = false;
//        for (int i=0; i<arr.length; i++) {
//            if (arr[i] == null)
//                break;
//            if (i == arr.length - 1) {
//                res[index] = arr[i];
//                break;
//            }
//            if (arr[i+1] != null && arr[i+1].equals(reverse(arr[i]))) {
//                i++;
//                isReverse = true;
//                continue;
//            }
//            res[index++] = arr[i];
//        }
//        if (isReverse)
//            res = dirReduc(res);
//        return Arrays.stream(res).filter(Objects::nonNull).toArray(String[]::new);
//    }

    //优化后
    public static String[] dirReduc(String[] arr) {
        List<String> list = new ArrayList<>(Arrays.asList(arr));
        for (int i = 1; i < list.size(); ++i) {
            if (i == 0)
                continue;
            if (reverse(list.get(i)).equals(list.get(i - 1))) {
                list.remove(i--);
                list.remove(i--);
            }
        }
        return list.toArray(String[]::new);
    }

    public static void main (String[] args) {
//        String[] temp = new String[]{"NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"};
        String[] temp = new String[]{"NORTH","SOUTH","SOUTH","EAST","WEST","NORTH"};
        System.out.println(Arrays.toString(dirReduc(temp)));
    }

}
