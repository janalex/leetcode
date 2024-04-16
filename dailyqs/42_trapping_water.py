from typing import List


class Solution:
    def trap(self, heights: List[int]) -> int:
        size = len(heights)
        l_heights = [0] * size
        r_heights = [0] * size
        l_heights[0] = heights[0]
        r_heights[-1] = heights[-1]

        for i in range(1, size):
            l_heights[i] = max(heights[i], l_heights[i - 1])
        for i in range(-2, -size-1, -1):
            r_heights[i] = max(heights[i], r_heights[i + 1])
        result = 0
        for i in range(size):
            result += min(l_heights[i], r_heights[i]) - heights[i]
        return result
    

testCases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.trap(test)}')
