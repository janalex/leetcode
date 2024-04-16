from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        total = sum(nums)
        for n in nums:
            if n >= total / 2:
                total -= n
            else:
                break
        return total if total else -1
    

testCases = [
    [5,5,5],
    [1,12,1,2,5,50,3],
    [5,5,50],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.largestPerimeter(test)}')