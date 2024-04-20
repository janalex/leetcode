from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []
        height = len(land)
        width = len(land[0])
        for x in range(height):
            for y in range(width):
                if land[x][y] == 1:
                    y1 = y + 1
                    while y1 < width and land[x][y1] == 1:
                        y1 += 1
                    x1 = x + 1
                    while x1 < height and land[x1][y] == 1:
                        x1 += 1
                    result.append([x, y, x1 - 1, y1 - 1])
                    for i in range(x, x1):
                        for j in range(y, y1):
                            land[i][j] = -1
        return result


testCases = [
    [[1, 0, 0], [0, 1, 1], [0, 1, 1]],
    [[1, 1], [1, 1]],
    [[0]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findFarmland(test)}')
