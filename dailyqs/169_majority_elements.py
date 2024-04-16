from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num = -1
        count = 0
        for n in nums:
            if count == 0:
                num = n
            if num == n:
                count += 1
            else:
                count -= 1
        return num
    

testCases = [
    [3,2,3],
    [2,2,1,1,1,2,2],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.majorityElement(test)}')
