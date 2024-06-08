from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = {0: -1}
        ps = [0] * len(nums)
        for i in range(len(nums)):
            ps[i] = (ps[i - 1] + nums[i]) % k
            if ps[i] in sums:
                if sums[ps[i]] < i - 1:
                    return True
            else:
                sums[ps[i]] = i
        return False


testCases = [
    ([0, 0], 1),
    ([23, 2, 4, 6, 6], 7),
    ([5, 0, 0, 0], 3),
    ([1, 2, 12], 6),
    ([23, 2, 4, 6, 7], 6),
    ([23, 2, 6, 4, 7], 6),
    ([23, 2, 6, 4, 7], 13),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.checkSubarraySum(*test)}')
