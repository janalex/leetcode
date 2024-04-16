from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result : List[List[int]] = []
        for i in range(0, len(nums), 3):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            if c - a > k:
                return []
            result.append([a, b, c])
        return result
    
testCases : List[tuple[List[int], int]] = [
    ([1,3,4,8,7,9,3,5,1], 2),
    ([1,3,3,2,7,3], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.divideArray(test[0], test[1])}')
