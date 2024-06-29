import bisect
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        n2ns: list[list[int]] = [[] for _ in range(n)]
        ns2n: list[list[int]] = [[] for _ in range(n)]
        for e in edges:
            n2ns[e[0]].append(e[1])
            ns2n[e[1]].append(e[0])
        leaves = []
        for i, desc in enumerate(n2ns):
            if not desc:
                leaves.append(i)
        result = [[] for _ in range(n)]
        for l in leaves:
            self._dfs(l, ns2n, result)
        return result

    def _dfs(self, node: int, graph: list[list[int]], result: list[list[int]]) -> None:
        if result[node]:
            return
        for desc in graph[node]:
            self._dfs(desc, graph, result)
            bisect.insort(result[node], desc)
        for desc in graph[node]:
            result[node] = self._merge(result[node], result[desc])

    def _merge(self, a: list[int], b: list[int]) -> list[int]:
        i = j = 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                result.append(b[j])
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1
        while i < len(a):
            result.append(a[i])
            i += 1
        while j < len(b):
            result.append(b[j])
            j += 1
        return result


testCases = [
    (8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]),
    (5, [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.getAncestors(*test)}')
