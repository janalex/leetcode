from typing import List


class Solution:
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        def helper(index: int, subset: list[int], result: list[list[int]]):
            if index == len(nums):
                return
            helper(index + 1, subset.copy(), result)
            subset.append(nums[index])
            result.append(subset.copy())
            helper(index + 1, subset, result)
        subsets = [[]]
        helper(0, [], subsets)
        return subsets

    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result: list[list[int]] = []
        for i in range(2 << n - 1):
            subset: list[int] = []
            for j in range(n):
                if i & 1 << j:
                    subset.append(nums[j])
            result.append(subset)
        return result


testCases = [
    [1, 2, 3],
    [1, 2, 3, 4],
    [0],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.subsets(test)}')
