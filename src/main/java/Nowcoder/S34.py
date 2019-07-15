# -*- coding:utf-8 -*-
"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
    @href https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c
"""

class Solution:

    def FirstNotRepeatingChar(self, s):
        if s is None or len(s) == 0:
            return -1

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

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1


s = Solution()
print(s.FirstNotRepeatingChar("google"))
print(s.FirstNotRepeatingChar("NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp"))
print(s.FirstNotRepeatingChar("aa"))
print(s.FirstNotRepeatingChar(""))
print(s.FirstNotRepeatingChar(None))

