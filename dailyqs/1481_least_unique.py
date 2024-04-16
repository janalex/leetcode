from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        freq = list(c.items())
        freq.sort(key=lambda i: i[1])
        sum = len(freq)
        for _, f in freq:
            if k - f < 0:
                break
            sum -= 1
            k -= f
        return sum


testCases = [
    ([5, 5, 4], 1),
    ([4, 3, 1, 1, 3, 3, 2], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findLeastNumOfUniqueInts(*test)}')
