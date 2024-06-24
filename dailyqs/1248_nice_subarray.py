from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        pf = {0: 1}
        count = 0
        result = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                count += 1
            if (count - k) in pf:
                result += pf[count - k]
            pf[count] = pf.get(count, 0) + 1
        return result


testCases = [
    ([1, 1, 2, 1, 1], 3),
    ([2, 4, 6], 1),
    ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numberOfSubarrays(*test)}')
