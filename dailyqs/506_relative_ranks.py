import heapq
from typing import List


class Solution:
    first_3 = ["Gold Medal", "Silver Medal", "Bronze Medal"]

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = [(-score[x], x) for x in range(len(score))]
        heapq.heapify(ranks)
        pos = 0
        result = ['' for _ in range(len(score))]
        while ranks:
            _, index = heapq.heappop(ranks)
            if pos < len(Solution.first_3):
                result[index] = Solution.first_3[pos]
            else:
                result[index] = str(pos + 1)
            pos += 1
        return result
    

testCases = [
    [5, 4, 3, 2, 1],
    [10, 3, 8, 9, 4],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findRelativeRanks(test)}')
