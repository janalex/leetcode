from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        freq = [(c, f) for c, f in count.items()]
        freq.sort(key=lambda item : item[1], reverse=True)
        result = [c * f for c, f in freq]
        return ''.join(result)
    
testCases = [
    "tree",
    "cccaaa",
    "Aabb",
]

s = Solution()
for test in testCases:
    print(f'\'{test}\': \'{s.frequencySort(test)}\'')
