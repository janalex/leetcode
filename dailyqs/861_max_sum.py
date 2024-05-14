from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for row in grid:
            if not row[0]:
                for i in range(len(row)):
                    row[i] = 1 - row[i]

        for i in range(1, len(grid[0])):
            count_1 = 0
            for j in range(len(grid)):
                if grid[j][i]:
                    count_1 += 1
            if count_1 < len(grid) - count_1:
                for j in range(len(grid)):
                    grid[j][i] = 1 - grid[j][i]
        
        sum = 0
        for row in grid:
            num = 0
            for bit in row:
                num <<= 1
                num += bit
            sum += num
        return sum


testCases = [
    [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]],
    [[0]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.matrixScore(test)}')
