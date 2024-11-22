from collections import deque
import sys
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        size = len(nums)
        prefix_sums = [0] * (size + 1)
        for i in range(1, size + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
        indices = deque()
        result = sys.maxsize

        for i in range(size + 1):
            # consume all candidates that are valid for the current index
            while indices and prefix_sums[i] - prefix_sums[indices[0]] >= k:
                result = min(result, i - indices.popleft())

            # remove indices with larger prefix sums from the back of the dequeue
            while indices and prefix_sums[i] <= prefix_sums[indices[-1]]:
                indices.pop()
            
            indices.append(i)
        
        return result if result < sys.maxsize else -1
    

testCases = [
    ([1], 1),
    ([1, 2], 4),
    ([2, -1, 2], 3),
    ([2, -1, 2, 1], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.shortestSubarray(*test)}')
