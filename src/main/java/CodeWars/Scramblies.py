# description: 乱中有序
# author: C.v.
# href: https://www.codewars.com/kata/scramblies
# date: 2019-1-8


from collections import Counter

# Timed Out
# def scramble(s1, s2):
#     if len(s1) < len(s2):
#         return False
#     temp = list(s1)
#     for t2 in list(s2):
#         if t2 not in temp:
#             return False
#         temp.remove(t2)
#     return True


def scramble(s1, s2):
    c = Counter(s1)
    c.subtract(Counter(s2))
    t = c.most_common()[-1]
    return t[1] == 0


print(scramble('qxerwpxgguiagdcwoazk', 'adizogegwaxckrqwgxpu'))


