class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        lettter_lens = [0] * 26
        result = 0
        for ch in s:
            index = ord(ch) - ord('a')
            start = max(0, index - k)
            end = min(25, k + index) + 1
            lettter_lens[index] = max(lettter_lens[start:end]) + 1
            result = max(result, lettter_lens[index])
        return result
    

testCases = [
    ("acfgbd", 2),
    ("abcd", 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.longestIdealString(*test)}')
