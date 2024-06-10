from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        ps = [0] * len(nums)
        result = 0
        for i in range(len(nums)):
            ps[i] = (ps[i - 1] + nums[i]) % k
            count = sums.get(ps[i], 0)
            result += count
            sums[ps[i]] = count + 1
        return result


testCases = [
    ([4, 5, 0, -2, -3, 1], 5),
    ([5], 9),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.subarraysDivByK(*test)}')
