# description: 我的朋友在作弊吗
# author: C.v.
# href: https://www.codewars.com/kata/is-my-friend-cheating
# date: 2019-1-3


def removNb(n):
    sum = (n + 1) * n / 2
    res = list()
    for a in range(1, n + 1):
        # 公式推导: a * b = sum - a - b
        b = (sum - a) / (a + 1)
        if b.is_integer() and b <= n:
            res.append((a, b))
    return res


print(removNb(26))
print(removNb(100))
