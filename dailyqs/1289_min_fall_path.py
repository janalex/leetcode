from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        min = min2 = 0
        min_col = -1
        for row in grid:
            row_min = row_min2 = min + 100
            row_min_col = -1
            for y, val in enumerate(row):
                val = min + val if y != min_col else min2 + val
                if val < row_min:
                    row_min2 = row_min
                    row_min = val
                    row_min_col = y
                elif val < row_min2:
                    row_min2 = val
            min = row_min
            min_col = row_min_col
            min2 = row_min2
        return min


testCases = [
    [[1, 99, 99], [0, 2, 1], [99, 99, 4]],
    [[-2, -18, 31, -10, -71, 82, 47, 56, -14, 42],
     [-95, 3, 65, -7, 64, 75, -51, 97, -66, -28],
     [36, 3, -62, 38, 15, 51, -58, -90, -23, -63],
     [58, -26, -42, -66, 21, 99, -94, -95, -90, 89],
     [83, -66, -42, -45, 43, 85, 51, -86, 65, -39],
     [56, 9, 9, 95, -56, -77, -2, 20, 78, 17],
     [78, -13, -55, 55, -7, 43, -98, -89, 38, 90],
     [32, 44, -47, 81, -1, -55, -5, 16, -81, 17],
     [-87, 82, 2, 86, -88, -58, -91, -79, 44, -9],
     [-96, -14, -52, -8, 12, 38, 84, 77, -51, 52]],
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[7]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minFallingPathSum(test)}')
