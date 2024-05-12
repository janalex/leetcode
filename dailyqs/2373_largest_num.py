from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = [[0] * (len(grid[0]) - 2) for _ in range(len(grid) - 2)]
        for x in range(1, len(grid) - 1):
            for y in range(1, len(grid[0]) - 1):
                local_max = 0
                for shift_x in [-1, 0, 1]:
                    for shift_y in [-1, 0, 1]:
                        local_max = max(local_max, grid[x + shift_x][y + shift_y])
                result[x - 1][y - 1] = local_max
        return result


testCases = [
    [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]],
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.largestLocal(test)}')
