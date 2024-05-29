class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        index = len(s) - 1
        while s[index] == "0":
            steps += 1
            index -= 1
        while index > 0:
            steps += 2
            index -= 1
            while index >= 0 and s[index] == '1':
                steps += 1
                index -= 1
        return steps


testCases = [
    "1101",
    "10",
    "1",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numSteps(test)}')
