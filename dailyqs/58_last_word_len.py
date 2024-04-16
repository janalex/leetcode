class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = 0
        trail = True
        for i in range(-1, -len(s) - 1, -1):
            if s[i] == ' ':
                if trail:
                    continue
                break
            trail = False
            result += 1
        return result
    
testCases = [
    "Hello World",
    "   fly me   to   the moon  ",
    "luffy is still joyboy",
    "   ",
    "a   ",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.lengthOfLastWord(test)}')
