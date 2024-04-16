from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return len(arr) * max(arr)
        
        size = len(arr)
        dp = [0] * (size + 1)

        for i in range(size):
            curr_sum = curr_max = 0
            for j in range(i, max(-1, i - k), -1):
                curr_max = max(curr_max, arr[j])
                curr_sum = max(curr_sum, curr_max * (i - j + 1) + dp[j])
            dp[i + 1] = curr_sum

        return dp[-1]
    
testCases = [
    ([1,15,7,9,2,5,10], 3),
    ([1,4,1,5,7,3,6,1,9,9,3], 4),
    ([1], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxSumAfterPartitioning(test[0], test[1])}')
