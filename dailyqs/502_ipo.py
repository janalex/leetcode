import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap_c = [(x, i) for i, x in enumerate(capital)]
        heap_p = []
        heapq.heapify(heap_c)
        for _ in range(k):
            while heap_c and heap_c[0][0] <= w:
                profit = profits[heapq.heappop(heap_c)[1]]
                heapq.heappush(heap_p, -profit)
            if not heap_p:
                break
            w += -heapq.heappop(heap_p)
        return w
    

testCases = [
    (2, 0, [1, 2, 3], [0, 1, 1]),
    (3, 0, [1, 2, 3], [0, 1, 2]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findMaximizedCapital(*test)}')
