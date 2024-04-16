from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        result = [0, 0]
        if nums[0] != 1:
            result[1] = 1
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                result[0] = nums[i]
            elif nums[i-1] + 1 < nums[i]:
                result[1] = nums[i] - 1
            if result[0] and result[1]:
                break
        if not result[1]:
            result[1] = nums[-1] + 1
        return result

testCases = [
    [1,2,2,4],
    [1,1],
    [2,2]
]
s = Solution()
for test in testCases:
    print(f'{s.findErrorNums(test)}')
