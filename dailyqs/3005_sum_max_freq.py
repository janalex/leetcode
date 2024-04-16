from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        freq = list(counter.values())
        freq.sort(reverse=True)

        result = max = freq[0]
        i = 1
        while i < len(freq) and freq[i] == max:
            result += freq[i]
            i += 1

        return result
    

testCases = [
    [1, 2, 2, 3, 1, 4],
    [1, 2, 3, 4, 5],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxFrequencyElements(test)}')
