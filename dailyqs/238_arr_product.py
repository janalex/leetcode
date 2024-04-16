from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size < 2:
            return nums

        result = [0] * size
        result[-1] = nums[size - 1]

        for i in range(size - 2, -1, -1):
            result[i] = nums[i] * result[i + 1]
        for i in range(1, size):
            nums[i] = nums[i - 1] * nums[i]

        first = result[1]
        last = nums[-2]
        for i in range(1, size - 1):
            result[i] = nums[i - 1] * result[i + 1]
        result[0] = first
        result[-1] = last
        return result
    

testCases = [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.productExceptSelf(test)}')
