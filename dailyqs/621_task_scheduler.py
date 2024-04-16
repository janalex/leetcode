from collections import Counter
import operator
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        freq = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)
        k = 1
        max_freq = freq[0][1]
        for i in range(1, len(freq)):
            if freq[i][1] < max_freq:
                break
            k += 1
        size = len(tasks)
        return max((n + 1) * (max_freq - 1) + k, size)
    

testCases: list[tuple[list[str], int]] = [
    (["A", "A", "A", "B", "B", "B"], 2),
    (["A", "C", "A", "B", "D", "B"], 1),
    (["A", "A", "A", "B", "B", "B"], 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.leastInterval(*test)}')
