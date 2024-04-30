class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        dp = [0] * 1024
        dp[0] = 1
        result = 0
        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            result += dp[mask]
            for j in range(10):
                result += dp[mask ^ (1 << j)]
            dp[mask] += 1
        return result
    

testCases = [
    "aba",
    "aabb",
    "he",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.wonderfulSubstrings(test)}')
