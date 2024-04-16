from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        maxRow, maxCol = len(grid), len(grid[0])

        # dp stores maximum number of collected cherries for a given combination of both bots positions
        # if bot #1 is on [i, j] and bot #2 is on [i, k], the lookup in dp for this combination is
        # dp[i][j][k]. dp[x][y][x] is -1 if the bots can't get to this position combination (so far)
        dp = [[[-1] * maxCol for _ in range(maxCol)] for _ in range(maxRow)]

        # mark the number of cherries collected given the starting position combination of both bots
        dp[0][0][maxCol - 1] = grid[0][0] + grid[0][maxCol - 1]

        for i in range(1, maxRow):
            for j in range(maxCol):
                for k in range(j + 1, maxCol): # bots don't need to cross their paths
                    for x in range(-1, 2): # possible moves for bot #1 to get to [i, j]
                        for y in range(-1, 2): # possible moves for bot #2 to get to [i, k]
                            if 0 <= j + x < maxCol and 0 <= k + y < maxCol: # is previous position combination valid?
                                # number of cherries collected by both bots given their position combination
                                possiblePrev = dp[i - 1][j + x][k + y]
                                if possiblePrev != -1: # could the bots even get to this pos combination?
                                    # remember the maximum possible cherries we can collect on this positions combination in dp
                                    dp[i][j][k] = max(dp[i][j][k], possiblePrev + grid[i][j] + (grid[i][k] if j != k else 0))

        # return the maximum possible cherries across all possible finishing bots' position combinations
        return max(max(row) for row in dp[maxRow - 1])

    def cherryPickup2(self, grid: List[List[int]]) -> int:
        self._maxRow, self._maxCol = len(grid), len(grid[0])
        self._grid = grid
        self._mem = [[[-1] * self._maxCol for _ in range(self._maxCol)] for _ in range(self._maxRow)]
        return self.__dfs(0, 0, self._maxCol - 1)

    def __dfs(self, row: int, col1: int, col2: int) -> int:
        if row >= self._maxRow or not(0 <= col1 < self._maxCol and 0 <= col2 < self._maxCol):
            # invalid position combination
            return 0

        # if we already determined the maximum for this position combination just return it
        if self._mem[row][col1][col2] != -1:
            return self._mem[row][col1][col2]

        current_max = -1
        for x in range(col1 - 1, col1 + 2):
            for y in range(col2 - 1, col2 + 2):
                # consider all possible moves of both bots
                if x < y: # no need to cross the paths
                    current_max = max(current_max, self.__dfs(row + 1, x, y))

        # add the cherries we collect on this position combination
        max_cherries = current_max + self._grid[row][col1] + (self._grid[row][col2] if col1 != col2 else 0)
        # remember the value
        self._mem[row][col1][col2] = max_cherries
        return max_cherries

testCases = [
    [[3,1,1],[2,5,1],[1,5,5],[2,1,1]],
    [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.cherryPickup(test)}')
    print(f'{test}: {s.cherryPickup2(test)}')
