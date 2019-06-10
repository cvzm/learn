# -*- coding:utf-8 -*-

"""
题目描述:  *** 时间效率
    数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。

输入描述:
    例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
    由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


    @href https://www.nowcoder.com/practice/e8a1b01a2df14cb2b228b30ee6a92163
"""


class Solution:

    def MoreThanHalfNum_Solution(self, numbers):
        size = int(len(numbers) / 2)
        li = {}
        for n in numbers:
            num = li[n] + 1 if li.get(n) is not None else 1
            if num > size:
                return n

            li[n] = num

        return 0

    # 为提高 result 0 时的效率， 排除不可能达到的情况
    def MoreThanHalfNum_Solution2(self, numbers):
        size = int(len(numbers) / 2)
        li = {}
        maximum = 0
        index = size
        for n in numbers:
            num = li[n] + 1 if li.get(n) is not None else 1
            if num > size:
                return n
            li[n] = num

            maximum = num if num > maximum else maximum
            if size - index < 0:
                if maximum < index - size:
                    break
                else:
                    index += 1

        return 0

    # 将空间复杂的降为 O(1)。 参考答案， 补充：容错校验
    def MoreThanHalfNum_Solution3(self, numbers):
        if numbers is None or len(numbers) == 0:
            return 0
        result = numbers[0]
        counts = 0
        for n in numbers:
            if result == n:
                counts += 1
            elif counts == 0:
                result = n
                counts = 1
            else:
                counts -= 1

        # 校验 result 出现此时是否大于 len(number) / 2
        size = len(numbers) / 2
        rCount = 0
        index = size
        for n in numbers:
            if n == result:
                rCount += 1
            if rCount > size:
                break
            if index - size > 0:
                if rCount < index - size:
                    break
                else:
                    index += 1

        if rCount <= size:
            return 0

        return result


s = Solution()
print(s.MoreThanHalfNum_Solution2([1,2,3,2,2,2,5,4,2]))

