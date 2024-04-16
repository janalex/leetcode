import math


class Solution:
    def numSquares(self, n: int) -> int:
        root = math.floor(math.sqrt(n)) + 1
        squares = [a**2 for a in range(1, root)]
        dp = [n for _ in range(n + 1)]
        dp[0] = 0

        for i in range(1, n + 1):
            for s in squares:
                if s > i:
                    break
                dp[i] = min(dp[i - s] + 1, dp[i])
        return dp[n]
    
testCases = [
    12,
    13,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numSquares(test)}')
