from typing import List


class Solution:
    def _can_place(self, position: list[int], force: int, m: int) -> bool:
        index = 0
        while m and index < len(position):
            start = index
            m -= 1
            index += 1
            while index < len(position) and position[index] - position[start] < force:
                index += 1
        return m == 0

    def maxDistance(self, position: List[int], m: int) -> int:
        if m == 2:
            return max(position) - min(position)
        position.sort()
        end = ((position[-1] - position[0]) // (m - 1)) + 1
        start = 0
        max_force = 0
        while start <= end:
            mid = (start + end) // 2
            if self._can_place(position, mid, m):
                max_force = mid
                start = mid + 1
            else:
                end = mid - 1
        return max_force


testCases = [
    ([79, 74, 57, 22], 4),
    ([1, 2, 3, 4, 7], 3),
    ([5, 4, 3, 2, 1, 1000000000], 2),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxDistance(*test)}')
