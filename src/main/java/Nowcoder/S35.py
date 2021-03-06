# -*- coding:utf-8 -*-
"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P
    @href https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5
"""


class Solution:

    def InversePairs(self, data):
        # 逆序对总数
        res = 0
        if len(data) < 1:
            return res
        # 已遍历的集合
        history = BinaryList()
        history.list = []
        history.list.append(data[0])
        for i in range(1, len(data)):
            # 校验是否为逆对
            n = data[i]
            index = history.binaryIndex(n)
            history.append(n)

            if index == 0:
                continue
            res += index

        return res % 1000000007


# 自定义「倒序」二分集合
class BinaryList:

    # 数据源
    list = []

    # 倒序添加
    def append(self, n):
        if len(self.list) == 0:
            self.append(n)
            return
        if n > self.list[0]:
            self.list.insert(0, n)
        elif n < self.list[-1]:
            self.list.append(n)
        else:
            i = self.binaryIndex(n)
            self.list.insert(i, n)

    # 二分查找下标, 返回当前index，无则返回 最终指针位置
    def binaryIndex(self, n):
        size = len(self.list)
        start, end = 0, size -1
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if self.list[mid] == n:
                return mid
            elif n > self.list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        # 校验大小偏移
        if n < self.list[mid]:
            mid += 1
        return mid


s = Solution()
# print(s.InversePairs([1,2,3,4,5,6,7,0]))
# print(s.InversePairs([1,2,4,3,7,6,5,0]))
print(s.InversePairs([627126,415347,850134,371085,279048,705820,453064,944751,92317,58592,167988,284065,992573,78043,190215,104546,607528,391775,701214,849731,231053,603058,975374,199773,479544,143961,206797,325662,90035,69615,429916,717161,484962,796403,604598,280362,502223,57662,741466,594540,632606,909454,394957,625180,503849,585172,729726,627729,976947,947293,477461,724352,66703,452835,440478,62599,596797,163627,388261,203184,233243,334529,436697,234557,647284,41295,514920,665859,615310,256386,776752,247916,682192,171709,389448,186041,273234,635527,813771,766533,582820,807584,490886,649523,260419,447716,228474,373568,611343,616735,576752,844586,467616,529801,595496,631253,571097,110416,297112,186407,883154,73864,950675,81698,245574,340124,267739,35160,975651,597862,801693,74823,921798,292579,240698,182218,256647,469172,72138,867991,602259,165243,228929,69875,695044,824425,701128,782493,451193,998241,485252,334347,588457,435928,416045,350383,292404,200137,385543,268055,314351,187237,859230,236150,996168,99928,9347]))
# print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))


