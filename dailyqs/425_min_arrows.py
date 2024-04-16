import operator
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = operator.itemgetter(0))
        count = 0
        i = 0
        while i < len(points):
            count += 1
            end = points[i][1]
            i += 1
            while i < len(points) and points[i][0] <= end:
                end = min(end, points[i][1])
                i += 1

        return count
    

testCases = [
    [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]],
    [[10, 16], [2, 8], [1, 6], [7, 12]],
    [[1, 2], [3, 4], [5, 6], [7, 8]],
    [[1, 2], [2, 3], [3, 4], [4, 5]],
    [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findMinArrowShots(test)}')
