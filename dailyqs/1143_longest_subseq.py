class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp : list[list[int]] = [[] for _ in range(len(text1))]
        for i in range(0, len(text1)):
            for j in range(0, len(text2)):
                if (text1[i] == text2[j]):
                    dp[i].append((dp[i-1][j-1] if j > 0 and i > 0 else 0) + 1)
                else:
                    dp[i].append(max(dp[i][j-1] if j > 0 else 0, dp[i-1][j] if i > 0 else 0))
        return dp[len(text1)-1][len(text2)-1]

testCases = [
    ["abcde", "ace"],
    ["abc", "abc"],
    ["abc", "def"]
]

s = Solution()
for test in testCases:
    print(f'{test[0]=}, {test[1]=}: {s.longestCommonSubsequence(test[0], test[1])}')
