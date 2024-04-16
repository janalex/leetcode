import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counts = [0] * n
        pq : List[tuple[int, int]] = [(-1, i) for i in range(n)]
        for meet in meetings:
            room = heapq.heappop(pq)
            # if there are unused rooms, force the sort by room number on those
            while room[0] < meet[0]:
                heapq.heappush(pq, (meet[0], room[1]))
                room = heapq.heappop(pq)
            counts[room[1]] += 1
            heapq.heappush(pq, (room[0] + meet[1] - meet[0], room[1]))
        max_count = max(counts)
        max_room = counts.index(max_count)
        return max_room

testCases = [
    (4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]]),
    (2, [[0, 10], [1, 5], [2, 7], [3, 4]]),
    (3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.mostBooked(*test)}')