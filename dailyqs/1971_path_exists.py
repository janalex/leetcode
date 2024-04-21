from collections import deque
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.__roots = [x for x in range(n)]

    def __find(self, i: int) -> int:
        r = self.__roots[i]
        if r == i:
            return r
        else:
            self.__roots[i] = self.__find(r)
            return self.__roots[i]

    def union(self, i: int, j: int) -> None:
        r1, r2 = self.__find(i), self.__find(j)
        if r1 == r2:
            return
        self.__roots[r2] = r1

    def connected(self, i: int, j: int) -> bool:
        return self.__find(i) == self.__find(j)


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)
        for e in edges:
            uf.union(e[0], e[1])
        return uf.connected(source, destination)

    def validPath1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[False, []] for _ in range(n)]
        for e in edges:
            graph[e[0]][1].append(e[1])
            graph[e[1]][1].append(e[0])
        q = deque([source])
        found = False
        while q:
            node = q.popleft()
            if node == destination:
                found = True
                break
            if graph[node][0]:
                continue
            graph[node][0] = True
            q.extend(graph[node][1])
        return found


testCases = [
    (3, [[0, 1], [1, 2], [2, 0]], 0, 2),
    (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.validPath(*test)}')
