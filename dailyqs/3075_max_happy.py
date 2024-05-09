import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        q = heapq.nlargest(k, happiness)
        sum = 0
        for i in range(k):
            if q[i] <= i:
                break
            sum += q[i] - i
        return sum


testCases = [
    ([1, 2, 3], 2),
    ([1, 1, 1, 1], 2),
    ([2, 3, 4, 5], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maximumHappinessSum(*test)}')
