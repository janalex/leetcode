import heapq
from typing import List


class Solution:
    def maxProfitAssignment1(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        heapq.heapify(jobs)
        profit_h = []
        worker.sort()
        result = 0
        for w in worker:
            while jobs and jobs[0][0] <= w:
                heapq.heappush(profit_h, -heapq.heappop(jobs)[1])
            if profit_h:
                result += -profit_h[0]
        return result

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_worker = max(worker)
        profit_diff = [0] * (max_worker + 1)
        for i in range(len(difficulty)):
            if difficulty[i] <= max_worker:
                profit_diff[difficulty[i]] = max(profit_diff[difficulty[i]], profit[i])
        for i in range(1, len(profit_diff)):
            profit_diff[i] = max(profit_diff[i], profit_diff[i - 1])
        result = 0
        for w in worker:
            result += profit_diff[w]
        return result


testCases = [
    ([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]),
    ([85, 47, 57], [24, 66, 99], [40, 25, 25]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxProfitAssignment(*test)}')
