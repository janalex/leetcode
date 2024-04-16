from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = Counter(s)
        for i, ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
    
testCases = [
    "leetcode",
    "loveleetcode",
    "aabb",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.firstUniqChar(test)}')
