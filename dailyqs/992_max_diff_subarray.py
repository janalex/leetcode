from typing import List


class Solution:
    def subarraysWithKDistinct1(self, nums: List[int], k: int) -> int:
        result = 0
        freq: dict[int, int] = {}
        left = 0
        for right in range(len(nums)):
            f = freq.get(nums[right], 0)
            freq[nums[right]] = f + 1
            if len(freq) > k:
                while len(freq) > k:
                    f = freq[nums[left]]
                    if f == 1:
                        del freq[nums[left]]
                    else:
                        freq[nums[left]] -= 1
                    left += 1
            if len(freq) == k:
                f = freq.copy()
                l = left
                while len(f) == k:
                    result += 1
                    if f[nums[l]] > 1:
                        f[nums[l]] -= 1
                    else:
                        del f[nums[l]]
                    l += 1
        return result

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.subarraysWithMaxKDistinct(nums, k) - self.subarraysWithMaxKDistinct(nums, k - 1)

    def subarraysWithMaxKDistinct(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        result = 0
        left = 0
        freq: dict[int, int] = {}
        for right in range(len(nums)):
            f = freq.get(nums[right], 0)
            freq[nums[right]] = f + 1
            while len(freq) > k:
                freq[nums[left]] -= 1
                if not freq[nums[left]]:
                    del freq[nums[left]]
                left += 1
            result += right - left + 1
        return result

testCases: list[tuple[list[int], int]] = [
    ([2, 1, 1, 1, 2], 1),
    ([1, 2, 1, 2, 3], 2),
    ([1, 2, 1, 3, 4], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.subarraysWithKDistinct(*test)}')
