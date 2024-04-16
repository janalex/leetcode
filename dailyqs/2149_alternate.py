from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        result = []
        p = 0
        sign = 1
        size = len(nums)
        indexes = [0, 0]
        for _ in range(size):
            while sign * nums[indexes[p]] < 0:
                indexes[p] += 1
            result.append(nums[indexes[p]])
            indexes[p] += 1
            sign *= -1
            p = (p + 1) % 2
        return result
    

testCases = [
    [3,1,-2,-5,2,-4],
    [-1,1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.rearrangeArray(test)}')
