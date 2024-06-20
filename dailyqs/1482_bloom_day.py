from typing import List


class Solution:
    def _num_of_flowers(self, bloomDay: List[int], day: int, k: int) -> int:
        count = 0
        flower_count = 0
        for d in bloomDay:
            if d <= day:
                count += 1
            else:
                count = 0
            if count == k:
                flower_count += 1
                count = 0
        return flower_count

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        start, end = min(bloomDay), max(bloomDay)
        min_days = -1
        while start <= end:
            mid = (start + end) // 2
            if self._num_of_flowers(bloomDay, mid, k) >= m:
                min_days = mid
                end = mid - 1
            else:
                start = mid + 1

        return min_days


testCases = [
    ([1, 10, 3, 10, 2], 3, 1),
    ([1, 10, 3, 10, 2], 3, 2),
    ([7, 7, 7, 7, 12, 7, 7], 2, 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minDays(*test)}')
