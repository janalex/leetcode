class Solution:
    def checkRecord(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[1 if x == 0 else 0 for _ in range(3)] for _ in range(2)] for x in range(2)]
        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    prev = (i - 1) & 1
                    ans = dp[prev][j][0]  # P
                    ans += dp[prev][j][k + 1] if k < 2 else 0  # L
                    ans += dp[prev][j + 1][0] if j == 0 else 0  # A
                    dp[i & 1][j][k] = ans % mod
        return dp[n & 1][0][0]


testCases = [
    2,
    1,
    5,
    10101,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.checkRecord(test)}')
