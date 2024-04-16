from collections import deque
from typing import List


class Solution:
    def maxSubarrayLength1(self, nums: List[int], k: int) -> int:
        left = -1
        result = 0
        freq: dict[int, tuple[int, deque]] = {}
        for right in range(len(nums)):
            f, indexes = freq.get(nums[right], (0, deque([])))
            if f == k:
                newLeft = indexes.popleft()
                indexes.append(right)
                left += 1
                if newLeft > left:
                    while left < newLeft:
                        f, indexes = freq[nums[left]]
                        f -= 1
                        indexes.popleft()
                        freq[nums[left]] = f, indexes
                        left += 1
                left = newLeft
            else:
                f += 1
                indexes.append(right)
                freq[nums[right]] = (f, indexes)
                result = max(result, right - left)
        return result

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = -1
        result = 0
        freq: dict[int, int] = {}
        for right in range(len(nums)):
            f = freq.get(nums[right], 0)
            if f == k:
                left += 1
                while nums[left] != nums[right]:
                    freq[nums[left]] -= 1
                    left += 1
            else:
                f += 1
                freq[nums[right]] = f
                result = max(result, right - left)

        return result


testCases = [
    ([1, 2, 2, 2, 4], 1),
    ([1, 2, 2], 1),
    ([1, 2, 2, 1, 3], 1),
    ([1, 2, 3, 1, 2, 3, 1, 2], 2),
    ([1, 2, 1, 2, 1, 2, 1, 2], 1),
    ([5, 5, 5, 5, 5, 5, 5], 4),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxSubarrayLength(*test)}')
