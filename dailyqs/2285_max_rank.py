import heapq
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        city_importance = [0] * n
        for road in roads:
            city_importance[road[0]] += 1
            city_importance[road[1]] += 1
        # ranks = [-v for v in city_importance]
        # heapq.heapify(ranks)
        city_importance.sort()
        cur_importance = 1
        total = 0
        for v in city_importance:
            total += v * cur_importance
            cur_importance += 1
        return total


testCases = [
    (5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]),
    (5, [[0, 3], [2, 4], [1, 3]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maximumImportance(*test)}')
