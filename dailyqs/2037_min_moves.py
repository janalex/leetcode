import heapq
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        heapq.heapify(seats)
        heapq.heapify(students)
        result = 0
        while seats:
            seat = heapq.heappop(seats)
            student = heapq.heappop(students)
            result += abs(seat - student)
        return result


testCases = [
    ([3, 1, 5], [2, 7, 4]),
    ([4, 1, 5, 9], [1, 3, 2, 6]),
    ([2, 2, 6, 6], [1, 3, 2, 6]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minMovesToSeat(*test)}')
