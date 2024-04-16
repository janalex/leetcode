from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                result.append(n)
            else:
                nums[n - 1] = -nums[n - 1]
        return result
    

testCases = [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [1, 1, 2],
    [1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findDuplicates(test)}')
