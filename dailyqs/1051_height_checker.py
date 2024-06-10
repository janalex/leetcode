from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = heights.copy()
        sorted_heights.sort()
        result = 0
        for i, h in enumerate(heights):
            if h != sorted_heights[i]:
                result += 1
        return result


testCases = [
    [1, 1, 4, 2, 1, 3],
    [5, 1, 2, 3, 4],
    [1, 2, 3, 4, 5],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.heightChecker(test)}')
