from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        odd_counted = False
        for c, f in count.items():
            if f % 2 == 0:
                result += f
            elif odd_counted:
                result += f - 1
            else:
                result += f
                odd_counted = True
        return result


testCases = [
    "abccccdd",
    "a",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.longestPalindrome(test)}')
