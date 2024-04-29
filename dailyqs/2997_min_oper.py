from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums_xor = 0
        result = 0
        for n in nums:
            nums_xor ^= n
        while k or nums_xor:
            if (k % 2) != (nums_xor % 2):
                result += 1
            k //= 2
            nums_xor //= 2
        return result


testCases = [
    ([2, 1, 3, 4], 1),
    ([2, 0, 2, 0], 0),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minOperations(*test)}')
