from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if nums[i] < 1:
                nums[i] = size + 1

        for i in range(size):
            n = abs(nums[i])
            if n > size:
                continue
            if nums[n - 1] > 0:
                nums[n - 1] *= -1

        for i in range(size):
            if nums[i] > 0:
                return i + 1
            
        return size + 1
    

testCases = [
    [1, 1],
    [1, 2, 0],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
    [1, 2, 3],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.firstMissingPositive(test)}')
