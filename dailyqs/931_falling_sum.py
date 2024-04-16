from typing import List


class Value:
    def __init__(self, value: int, parentIndex: int) -> None:
        self.value = value
        self.parentIndex = parentIndex

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        size = len(matrix)
        m = [[0] * size for _ in range(size)]
        for i in range(size):
            m[0][i] = matrix[0][i]
        for i in range(1, size):
            for j in range(size):
                smallest = min(m[i-1][max(0, j - 1)], m[i-1][j], m[i-1][min(size-1, j + 1)])
                m[i][j] = matrix[i][j] + smallest
        return min(m[size-1])
    
testCases = [
    [[2,1,3],[6,5,4],[7,8,9]],
    [[-19,57],[-40,-5]]
]

s = Solution()
for test in testCases:
    print(f'{s.minFallingPathSum(test)}')
