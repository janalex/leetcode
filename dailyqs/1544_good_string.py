class Solution:
    def makeGood(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) == 0:
                result.append(c)
            elif abs(ord(c) - ord(result[-1])) == 32:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)


testCases = [
    "leEeetcode",
    "abBAcC",
    "aABbc",
    "s",
    "",
]

s = Solution()
for test in testCases:
    print(f'{test}: "{s.makeGood(test)}"')
