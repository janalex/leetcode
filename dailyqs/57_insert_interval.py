from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        size = len(intervals)
        result = []
        i = 0
        while i < size and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        if i == size or newInterval[1] < intervals[i][0]:
            result.append(newInterval)
        else :
            mergedInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
            while i < size and intervals[i][0] <= newInterval[1]:
                mergedInterval[1] = max(mergedInterval[1], intervals[i][1])
                i += 1
            result.append(mergedInterval)

        while i < size:
            result.append(intervals[i])
            i += 1

        return result
    

testCases = [
    ([[1, 5]], [0, 0]),
    ([[1, 3], [6, 9]], [2, 5]),
    ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.insert(*test)}')
