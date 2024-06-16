from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        max_possible = 0
        added_count = 0
        index = 0
        while max_possible < n and index < len(nums):
            while max_possible < min(nums[index] - 1, n):
                max_possible += max_possible + 1
                added_count += 1
            max_possible += nums[index]
            index += 1
        while max_possible < n:
            max_possible += max_possible + 1
            added_count += 1
        return added_count


testCases = [
    ([1, 2, 31, 33], 2147483647),
    ([1, 3], 6),
    ([1, 5, 10], 20),
    ([1, 2, 2], 5),
    ([1, 2, 2, 6, 34, 38, 41, 44, 47, 47, 56, 59, 62, 73, 77, 83, 87, 89, 94], 20),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minPatches(*test)}')
