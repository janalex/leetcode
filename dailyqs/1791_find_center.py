from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        nodes = {}
        for i in range(2):
            for j in range(2):
                nodes[edges[i][j]] = nodes.setdefault(edges[i][j], 0) + 1
        for k, v in nodes.items():
            if v == 2:
                return k
        return -1 # invalid graph


testCases = [
    [[1, 2], [2, 3], [4, 2]],
    [[1, 2], [5, 1], [1, 3], [1, 4]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findCenter(test)}')
