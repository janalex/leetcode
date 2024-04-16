from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_el = max(nums)
        result = 0
        freq = 0
        l_indexes = deque([])
        for right in range(len(nums)):
            if nums[right] == max_el:
                freq += 1
                l_indexes.append(right)
                if freq > k:
                    l_indexes.popleft()
            if freq >= k:
                result += l_indexes[0] + 1

        return result


testCases =[
    ([1, 3, 2, 3, 3], 2),
    ([1, 4, 2, 1], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countSubarrays(*test)}')
