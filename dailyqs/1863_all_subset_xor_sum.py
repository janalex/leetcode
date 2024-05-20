from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recursiveSum(index: int, current_sum: int, result: list[int]) -> None:
            if index == len(nums):
                return
            recursiveSum(index + 1, current_sum, result)
            result[0] += current_sum ^ nums[index]
            recursiveSum(index + 1, current_sum ^ nums[index], result)
        total = [0]
        recursiveSum(0, 0, total)
        return total[0]

testCases = [
    [1, 3],
    [5, 1, 6],
    [3, 4, 5, 6, 7, 8],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.subsetXORSum(test)}')
