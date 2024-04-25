from collections import deque
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph: dict[int, list[int]] = {}
        nodes: list[int] = [0] * n
        for e in edges:
            ne = graph.get(e[0], [])
            ne.append(e[1])
            graph[e[0]] = ne
            ne = graph.get(e[1], [])
            ne.append(e[0])
            graph[e[1]] = ne
            nodes[e[0]] += 1
            nodes[e[1]] += 1
        q: deque[tuple[int, int]] = deque([(node, 0) for node in range(n) if nodes[node] == 1])
        result = []
        size = n
        while q:
            node, rank = q.popleft()
            size -= 1
            if not size:
                result = [node]
                break
            if size == 1 and q[0][1] == rank:
                result = [node, q.popleft()[0]]
                break
            nodes[node] -= 1
            for next in graph[node]:
                nodes[next] -= 1
                if nodes[next] == 1:
                    q.append((next, rank + 1))
        return result


testCases = [
    (1, []),
    (2, [[0, 1]]),
    (4, [[1, 0], [1, 2], [1, 3]]),
    (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findMinHeightTrees(*test)}')
