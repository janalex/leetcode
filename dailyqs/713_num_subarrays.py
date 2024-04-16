from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        start = 0
        end = 0
        product = nums[end]
        result = 0
        while True:
            p = product
            if p < k:
                result += end - start + 1
            else:
                product //= nums[start]
                start += 1

            if p < k or start > end:
                end += 1
                if end == len(nums):
                    break
                product *= nums[end]

        return result


testCases = [
    ([10, 5, 2, 6], 100),
    ([1, 2, 3], 0),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numSubarrayProductLessThanK(*test)}')
