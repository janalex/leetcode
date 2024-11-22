from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = Counter(arr)
        for s in arr:
            if freq[s] == 1:
                k -= 1
                if not k:
                    return s
        return ''


testCases = [
    (["d", "b", "c", "b", "c", "a"], 2),
    (["aaa", "aa", "a"], 1),
    (["a", "b", "a"], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: "{s.kthDistinct(*test)}"')
