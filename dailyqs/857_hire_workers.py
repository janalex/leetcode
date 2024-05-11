import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ratios = sorted([(w / q, q) for w, q in zip(wage, quality)])
        heap: list[int] = []
        q_sum = 0
        max_ratio = 0.0
        for i in range(k):
            max_ratio = max(max_ratio, ratios[i][0])
            q_sum += ratios[i][1]
            heapq.heappush(heap, -ratios[i][1])

        result = max_ratio * q_sum

        for i in range(k, len(quality)):
            max_ratio = max(max_ratio, ratios[i][0])
            q_sum += ratios[i][1] + heapq.heappop(heap)
            heapq.heappush(heap, -ratios[i][1])
            result = min(result, q_sum * max_ratio)

        return result


testCases = [
    ([10, 20, 5], [70, 50, 30], 2),
    ([3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.mincostToHireWorkers(*test)}')
