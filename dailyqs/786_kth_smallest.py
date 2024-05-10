import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        size = len(arr)
        heap = [(arr[x] / arr[-1], x, size - 1) for x in range(size - 1)]
        heapq.heapify(heap)
        frac = (0.0, 0, 0)
        while k > 0:
            frac = heapq.heappop(heap)
            new_y = frac[2] - 1
            if new_y > frac[1]:
                heapq.heappush(heap, (arr[frac[1]] / arr[new_y], frac[1], new_y))
            k -= 1
        return [arr[frac[1]], arr[frac[2]]]


testCases = [
    ([1, 2, 3, 5], 3),
    ([1, 7], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.kthSmallestPrimeFraction(*test)}')
