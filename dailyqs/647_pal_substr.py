class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return size

        dp = [[False * j for j in range(size - i + 1)] for i in range(size + 1)]
        for i in range(2):
            for j in range(size-i+1):
                dp[i][j] = True

        result = size
        for l in range(2, size + 1):
            for i in range(size - l + 1):
                if dp[l-2][i+1] and s[i] == s[i + l - 1]:
                    dp[l][i] = True
                    result += 1

        return result
    
testCases = [
    "abc",
    "aaa",
    "abccba",
    "a"
]

s = Solution()
for test in testCases:
    print(f'\'{test}\': \'{s.countSubstrings(test)}\'')