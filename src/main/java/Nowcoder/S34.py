# -*- coding:utf-8 -*-

"""

在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
    @href https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c
"""

class Solution:

    def FirstNotRepeatingChar(self, s):
        d = {}  # 字典使用 hash table, 理想查询负载度 O(1), 从而代替list
        for c in s:
            ''' 3. 使用get默认值方法 '''
            d[c] = d.get(c, 0) + 1

            ''' 2. 使用try，性能会比遍历高 '''
            # try:
            #     d[c] += 1
            # except KeyError:
            #     d[c] = 1

            ''' 1. 相比其他，多了遍历操作 '''
            # if c not in d:
            #     d[c] = 0
            # d[c] += 1

        ''' 同值排序的顺序不靠谱，首环境影响， 而且此处也没必要排序。'''
        # s.index(sorted(d, key=lambda x: d[x])[0])

        ''' python 2/3 的字典排序算法不一致，导致遍历字典时， 不同版本的python无法保证 顺序一致性，从而无法满足第一个元素的条件， 。'''
        # for i in d:
        #     if d[i] == 1:
        #         return s.index(i)

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


s = Solution()
print(s.FirstNotRepeatingChar("google"))
print(s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))

