from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        if len(nums) < 3:
            return max(nums[0], nums[1])
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])
    
testCases = [
    [0],
    [1,2,3,1],
    [2,7,9,3,1],
    [1,7,9,2]
]
s = Solution()
for test in testCases:
    print(f'{s.rob(test)}')
