from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        result = ''
        for c in order:
            f = counter.get(c)
            if f:
                result += c * f
                del counter[c]
        for c in counter.elements():
            result += c
        return result
    

testCases = [
    ('cba', 'abcd'),
    ('bcafg', 'abcd'),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.customSortString(*test)}')
