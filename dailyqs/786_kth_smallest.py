import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        size = len(arr)
        heap = [(arr[x] / arr[-1], x, size - 1) for x in range(size - 1)]
        heapq.heapify(heap)
        while k > 0:
            _, x, y = heapq.heappop(heap)
            new_y = y - 1
            if new_y > x:
                heapq.heappush(heap, (arr[x] / arr[new_y], x, new_y))
            k -= 1
        return [arr[x], arr[y]]


testCases = [
    ([1, 2, 3, 5], 3),
    ([1, 7], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.kthSmallestPrimeFraction(*test)}')
