from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        neg_nums = set()
        for n in nums:
            if n < 0:
                neg_nums.add(n)
        max = -1
        for n in nums:
            if n > max and -n in neg_nums:
                max = n
        return max
    

testCases = [
    [-1,2,-3,3],
    [-1,10,6,7,-7,1],
    [-10,8,6,7,-2,-3],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findMaxK(test)}')
