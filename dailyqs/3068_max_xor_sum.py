import sys
from typing import List


class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        min_diff = sys.maxsize
        odd = False
        result = 0
        for n in nums:
            if n < n ^ k:
                odd = not odd
                result += n ^ k
            else:
                result += n
            min_diff = min(min_diff, abs((n ^ k) - n))
        if odd:
            result -= min_diff
        return result


testCases = [
    ([24, 78, 1, 97, 44], 6, [[0, 2], [1, 2], [4, 2], [3, 4]]),
    ([1, 2, 1], 3, [[0, 1], [0, 2]]),
    ([2, 3], 7, [[0, 1]]),
    ([7, 7, 7, 7, 7, 7], 3, [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maximumValueSum(*test)}')
