from typing import List


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    result += 4
                    if x > 0 and grid[x - 1][y] == 1:
                        result -= 2
                    if y > 0 and grid[x][y - 1] == 1:
                        result -= 2
        return result

    def islandPerimeter1(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        found = False
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][j] == 1:
                    found = True
                    break
            if found:
                break
        if not found:
            return 0
        return self._dfs(i, j)

    def check_position(self, x, y) -> int:
        result = 0
        if 0 <= x < self.height and 0 <= y < self.width:
            g_val = self.grid[x][y]
            if not g_val:
                result = 1
            elif g_val == 1:
                result = self._dfs(x, y)
        else:
            result = 1
        return result

    def _dfs(self, x: int, y: int) -> int:
        self.grid[x][y] = -1
        result = 0
        for i in [-1, 1]:
            result += self.check_position(x + i, y)
            result += self.check_position(x, y + i)
        return result


testCases = [
    [[1], [0]],
    [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],
    [[1]],
    [[1, 0]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.islandPerimeter(test)}')
