from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        correct_sum = (size + 1) * size // 2
        real_sum = sum(nums)
        return correct_sum - real_sum


testCases = [
    [3, 0, 1],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.missingNumber(test)}')
