from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        left = right = 0
        foundMin = foundMax = False
        valid_subs = []
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                if foundMin and foundMax:
                    valid_subs.append((left, right))
                right = left = i + 1
                foundMin = foundMax = False
            else:
                if nums[i] == minK:
                    foundMin = True
                if nums[i] == maxK:
                    foundMax = True
                right = i + 1
        if foundMin and foundMax:
            valid_subs.append((left, right))
        
        for l, r in valid_subs:
            result += self.countSubarraysValid(nums[l:r], minK, maxK)
        return result
    
    def countSubarraysValid(self, nums: list[int], minK: int, maxK: int) -> int:
        result = 0
        min_i = max_i = -1
        for i in range(len(nums)):
            if nums[i] == minK:
                min_i = i
            if nums[i] == maxK:
                max_i = i
            if min_i >= 0 and max_i >= 0:
                result += max(min_i, max_i) - abs(max_i - min_i) + 1

        return result

    def countSubarrays1(self, nums: List[int], minK: int, maxK: int) -> int:
        return self.countSubarraysMaxK(nums, maxK) - self.countSubarraysMaxK(nums, minK)

    def countSubarraysMaxK(self, nums: list[int], maxK: int) -> int:
        result = 0
        left = 0
        last_k = -1

        for right in range(len(nums)):
            if nums[right] == maxK:
                last_k = right
            if nums[right] <= maxK and last_k > -1:
                result += last_k - left + 1
            if nums[right] > maxK:
                last_k = -1
                left = right

        return result
    

testCases: list[tuple[list[int], int, int]] = [
    ([1, 3, 5, 2, 7, 5], 1, 5),
    ([1, 1, 1, 1], 1, 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countSubarrays(*test)}')
