from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ps = {0 : -1}
        result = 0
        diff = 0
        for i, n in enumerate(nums):
            if n:
                diff += 1
            else:
                diff -= 1
            pos = ps.get(diff, -2)
            if pos >= -1:
                result = max(result, i - pos)
            else:
                ps[diff] = i

        return result
    

testCases = [
    [0, 1],
    [0, 1, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 0, 0],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findMaxLength(test)}')
