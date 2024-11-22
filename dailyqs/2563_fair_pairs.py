from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums: List[int], maximum: int) -> int:
        result = left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < maximum:
                result += right - left
                left += 1
            else:
                right -= 1
        return result


testCases = [
    ([0, 1, 7, 4, 4, 5], 3, 6),
    ([1, 7, 9, 2, 5], 11, 11),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countFairPairs(*test)}')
