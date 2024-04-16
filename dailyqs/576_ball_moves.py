CAP = 10**9 + 7

class Solution:
    dp: list[list[list[int]]]
    dpNew: list[list[list[int]]]

    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0

        self.dpNew = [[[0, 0] for _ in range(n)] for _ in range(m)]
        self.dp = self.dpNew
        self.maxX = m - 1
        self.maxY = n - 1
        self.dp[startRow][startColumn][1] = 1
        self.setNeighbors(startRow, startColumn, 1, 1)
        result = self.countOutMoves(startRow, startColumn)
        self.dp = self.dpNew
        for move in range(1, maxMove):
            self.copyDp()
            for x in range(self.maxX + 1):
                for y in range(self.maxY + 1):
                    if self.dp[x][y][0] == move:
                        result += self.countOutMoves(x, y)
                        result %= CAP
                        self.setNeighbors(x, y, move + 1, self.dp[x][y][1])
            self.dp = self.dpNew
                            
        return result
    
    def copyDp(self):
        self.dpNew = self.dp.copy()
        for i in range(self.maxX + 1):
            self.dpNew[i] = self.dp[i].copy()
            for j in range(self.maxY + 1):                
                self.dpNew[i][j] = self.dp[i][j].copy()
                self.dpNew[i][j][1] = 0

    def countOutMoves(self, x: int, y: int):
        result = 0
        if x == 0:
            result += 1
        if x == self.maxX:
            result += 1
        if y == 0:
            result += 1
        if y == self.maxY:
            result += 1
        return result * self.dp[x][y][1]

    def setNeighbors(self, x: int, y: int, value: int, paths: int):
        if self.maxX > 0:
            match x:
                case 0:
                    self.dpNew[x+1][y][0] = value
                    self.dpNew[x+1][y][1] += paths
                case _x if _x == self.maxX:
                    self.dpNew[x-1][y][0] = value
                    self.dpNew[x-1][y][1] += paths
                case _:
                    self.dpNew[x-1][y][0] = value
                    self.dpNew[x-1][y][1] += paths
                    self.dpNew[x+1][y][0] = value
                    self.dpNew[x+1][y][1] += paths
        if self.maxY > 0:
            match y:
                case 0:
                    self.dpNew[x][y+1][0] = value
                    self.dpNew[x][y+1][1] += paths
                case _y if _y == self.maxY:
                    self.dpNew[x][y-1][0] = value
                    self.dpNew[x][y-1][1] += paths
                case _:
                    self.dpNew[x][y-1][0] = value
                    self.dpNew[x][y-1][1] += paths
                    self.dpNew[x][y+1][0] = value
                    self.dpNew[x][y+1][1] += paths
    
testCases = [
    [2, 3, 8, 1, 0],
    [2, 2, 2, 0, 0],
    [1, 3, 3, 0, 1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findPaths(*test)}')
