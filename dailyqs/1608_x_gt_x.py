from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        i = 0
        while i < size and size - i > nums[i]:
            i += 1
        return size - i if i < size and (i == 0 or nums[i - 1] < size - i) else -1


testCases = [
    [3, 6, 7, 7, 0],
    [3, 5],
    [0, 0],
    [0, 4, 3, 0, 4],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.specialArray(test)}')
