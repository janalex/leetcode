from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psf: dict[int, int] = {0: 1}
        sum = 0
        result = 0
        for n in nums:
            sum += n
            freq = psf.get(sum - goal, 0)
            result += freq
            psf[sum] = psf.get(sum, 0) + 1

        return result


testCases: list[tuple[list[int], int]] = [
    ([1, 0, 1, 0, 1], 2),
    ([0, 0, 0, 0, 0], 0),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numSubarraysWithSum(*test)}')
