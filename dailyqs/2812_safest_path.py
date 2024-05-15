from collections import deque
from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self._root = [x for x in range(n)]
        self._rank = [1] * n

    def find(self, x: int) -> int:
        if x == self._root[x]:
            return x
        else:
            self._root[x] = self.find(self._root[x])
            return self._root[x]

    def union(self, x: int, y: int) -> None:
        rX, rY = self.find(x), self.find(y)
        if rX == rY:
            return
        if self._rank[rX] > self._rank[rY]:
            rX, rY = rY, rX
        self._root[rX] = rY
        if self._rank[rX] == self._rank[rY]:
            self._rank[rY] += 1

    def connected(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        size = len(grid)

        def to1d(x: int, y: int) -> int:
            return x * size + y

        if grid[0][0] or grid[size - 1][size - 1]:
            return 0
        q: deque[tuple[int, int]] = deque()
        for i in range(size):
            for j in range(size):
                if grid[i][j]:
                    grid[i][j] = 0
                    q.append((i, j))
                else:
                    grid[i][j] = -1

        dist2cell = [[] for _ in range(800)]  # maximum distance given the limits
        dist = 0
        while q:
            q_size = len(q)
            for _ in range(q_size):
                x, y = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    a, b = x + dx, y + dy
                    if 0 <= a < size and 0 <= b < size and grid[a][b] == -1:
                        grid[a][b] = dist + 1
                        q.append((a, b))
                        dist2cell[dist + 1].append((a, b))
            dist += 1

        g = UnionFind(size * size)
        for dd in range(dist - 1, -1, -1):
            if not dist2cell[dd]:
                continue
            for x, y in dist2cell[dd]:
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    a, b = x + dx, y + dy
                    if 0 <= a < size and 0 <= b < size and grid[a][b] >= dd:
                        g.union(to1d(x, y), to1d(a, b))
            if g.connected(0, to1d(size - 1, size - 1)):
                return dd
        return 0


testCases = [
    [[1, 0, 0], [0, 0, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maximumSafenessFactor(test)}')
