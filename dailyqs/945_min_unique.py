from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        freq = [0] * (len(nums) + max(nums) + 1)
        for n in nums:
            freq[n] += 1
        result = 0
        for i in range(len(freq)):
            if freq[i] > 1:
                increments = freq[i] - 1
                freq[i + 1] += increments
                result += increments
        return result


testCases = [
    [2, 2, 2, 1],
    [1, 2, 2],
    [3, 2, 1, 2, 1, 7],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minIncrementForUnique(test)}')
