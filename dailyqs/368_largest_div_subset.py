from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp : List[tuple[int, int, tuple|None]] = []
        nums.sort()
        max_sub : tuple|None = None
        for i in nums:
            max_count = 1
            max_last = None
            for num in reversed(dp):
                if i % num[0] == 0 and num[1] >= max_count:
                    max_count = num[1] + 1
                    max_last = num
            cur = (i, max_count, max_last)
            dp.append(cur)
            if not max_sub or max_count > max_sub[1]:
                max_sub = cur

        result = []
        next = max_sub
        while next:
            result.append(next[0])
            next = next[2]
        return result
    

testCases = [
    [1,2,3],
    [1,2,4,8],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.largestDivisibleSubset(test)}')
