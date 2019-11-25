# -*- coding:utf-8 -*-
"""
 * 题目描述
 *     给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
 *     例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
 *     那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}；
 *      针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
 *       {[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}，
 *       {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
 *
 *     @href https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788
"""


class Solution:

    def maxInWindows(self, num, size):
        if len(num) < size or size == 0:
            return []

        res = []
        for i in range(0, len(num) - size + 1):
            max_num = None
            for j in range(i, i + size):
                max_num = num[j] if num[j] > max_num else max_num

            res.append(max_num)

        return res


res = Solution().maxInWindows([2,3,4,2,6,2,5,1],3)
print res