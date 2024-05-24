from collections import Counter
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = [0] * (nums[-1] + 1)
        def recurse(index: int) -> int:
            if index == len(nums):
                return 1
            ret = recurse(index + 1)
            if nums[index] >= k and count[nums[index] - k]:
                return ret
            count[nums[index]] += 1
            ret += recurse(index + 1)
            count[nums[index]] -= 1
            return ret
        return recurse(0) - 1


testCases = [
    ([2, 4, 6], 2),
    ([1], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.beautifulSubsets(*test)}')
