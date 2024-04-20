from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        result = 0
        for x in range(self.height):
            for y in range(self.width):
                if self.grid[x][y] == '1':
                    result += 1
                    self._dfs(x, y)
        return result

    def _check_position(self, x: int, y: int):
        if 0 <= x < self.height and 0 <= y < self.width and self.grid[x][y] == '1':
            self._dfs(x, y)

    def _dfs(self, x: int, y: int):
        self.grid[x][y] = 'x'
        for i in [-1, 1]:
            self._check_position(x + i, y)
            self._check_position(x, y + i)


testCases = [
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]],
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numIslands(test)}')
