# -*- coding:utf-8 -*-
"""
    请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
        路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
        如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。
        例如 a b c e s f c s a d e e 矩阵中包含一条字符串"bcced"的路径，
        但是矩阵中不包含"abcb"路径，
        因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。

    @href https://www.nowcoder.com/practice/c61c6999eecb4b8f88a98f66b273a3cc
"""


class Solution:

    def hasPath(self, matrix, rows, cols, path):
        # 构造矩阵
        m = []
        c = 0
        for i in range(rows):
            l = []
            for j in range(cols):
                l.append(matrix[c])
                c += 1
            m.append(l)
        d = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # 定义dfs函数
        def dfs(x, y, path):
            if not path:
                return True
            for dx, dy in d:
                if 0 <= x + dx < rows and \
                        0 <= y + dy < cols and \
                        (x + dx, y + dy) not in visited and m[x + dx][y + dy] == path[0]:
                    visited.add((x + dx, y + dy))
                    if dfs(x + dx, y + dy, path[1:]):
                        return True
                    visited.remove((x + dx, y + dy))

        # 已经走过的路记录下来
        visited = set()
        for i in range(rows):
            for j in range(cols):
                # 以第一个字母为起点
                if m[i][j] == path[0]:
                    visited.add((i, j))
                    if dfs(i, j, path[1:]):
                        return True
                    visited.remove((i, j))


Solution().hasPath("ABCESFCSADEE",3,4,"ABCCED")