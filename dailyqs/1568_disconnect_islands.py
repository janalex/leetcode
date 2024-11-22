from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        return 0


testCases = [
    [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
    [[1, 1]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minDays(test)}')
