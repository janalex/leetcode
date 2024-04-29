from typing import List


class Solution:
    def buildCountAndSum(self, node: int, parent: int = -1) -> None:
        for n in self.adj[node]:
            if n == parent:
                continue
            self.buildCountAndSum(n, node)
            self.count[node] += self.count[n]
            self.sum[node] += self.sum[n] + self.count[n]

    def reroot(self, node: int, parent: int = -1) -> None:
        for n in self.adj[node]:
            if n == parent:
                continue
            self.sum[n] = self.sum[node] + self.size - 2 * self.count[n]
            self.reroot(n, node)

    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.size = n
        self.count = [1] * n
        self.sum = [0] * n
        self.adj: list[list[int]] = [[] for _ in range(n)]
        for e in edges:
            self.adj[e[0]].append(e[1])
            self.adj[e[1]].append(e[0])
        self.buildCountAndSum(0)
        self.reroot(0)
        return self.sum


testCases = [
    (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]),
    (1, []),
    (2, [[1, 0]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.sumOfDistancesInTree(*test)}')
