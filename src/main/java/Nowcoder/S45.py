# -*- coding:utf-8 -*-
"""
题目描述
    LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...
    他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！
    “红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....
    LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
    上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。
    现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何，
    如果牌能组成顺子就输出true，否则就输出false。为了方便起见,你可以认为大小王是0。

    @href https://www.nowcoder.com/practice/762836f4d43d43ca9deb273b3de8e1f4
"""


class Solution:

    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False

        # 最大值，最小值, 0出现的次数
        min_num, max_num, count0 = 0, 0, 0
        for n in numbers:
            if n == 0:
                count0 += 1
                continue
            if n < min_num or min_num == 0:
                min_num = n
            elif n > max_num:
                max_num = n

        # 最大偏差值 ，即满足"顺子"的最大限制
        max_deviation = len(numbers) - 1

        # 校验是否只有一个有效数
        if count0 > max_deviation - 1:
            return True

        # 当前偏差值
        deviation = max_num - min_num

        return deviation == max_deviation or deviation + count0 == max_deviation


s = Solution()
# print(s.IsContinuous([0,3,1,6,4]))
# print(s.IsContinuous([0,3,2,6,4]))
print(s.IsContinuous([1,2,0,0,0]))
# print(s.IsContinuous([1,3,2,6,4]))
# print(s.IsContinuous([6,2,0,5,4]))
# print(s.IsContinuous([1,3,2,5,4]))
# print(s.IsContinuous([3,0,0,0,0]))
