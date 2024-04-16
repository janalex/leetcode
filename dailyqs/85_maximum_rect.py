from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        width = len(matrix[0])
        row = [0] * (width + 1)
        max_size = 0
        for i in range(len(matrix)):
            for j in range(width):
                row[j] = 1 + row[j] if matrix[i][j] == '1' else 0

            stack = []
            for j in range(width + 1):
                while stack and row[j] < row[stack[-1]]:
                    h = row[stack.pop()]
                    w = j if not stack else j - stack[-1] - 1
                    max_size = max(max_size, h * w)
                stack.append(j)
        return max_size
    

testCases = [
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]],
    [["0"]],
    [["1"]],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maximalRectangle(test)}')
