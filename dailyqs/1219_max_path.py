from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.grid = grid
        result = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] > 0:
                    result = max(result, self._dfs(x, y))
        return result

    def _dfs(self, x: int, y: int) -> int:
        gold = self.grid[x][y]
        self.grid[x][y] = 0
        result = gold
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(self.grid) and 0 <= new_y < len(self.grid[x]) and self.grid[new_x][new_y] > 0:
                result = max(result, gold + self._dfs(new_x, new_y))
        self.grid[x][y] = gold
        return result


testCases = [
    [[0, 6, 0], [5, 8, 7], [0, 9, 0]],
    [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.getMaximumGold(test)}')
