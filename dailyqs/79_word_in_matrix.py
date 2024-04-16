from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self._board = board
        self._word = word

        for i in range(len(board)):
            for j in range(len(board[i])):
                if self.__dps(i, j, 0):
                    return True
        return False
    
    def __dps(self, x: int, y: int, index: int) -> bool:
        if index == len(self._word):
            return True
        if not 0 <= x < len(self._board) or not 0 <= y < len(self._board[x]):
            return False

        if self._board[x][y] == self._word[index]:
            old_c = self._board[x][y]
            self._board[x][y] = chr(0)
            for i in [-1, 1]:
                if self.__dps(x + i, y, index + 1) or self.__dps(x, y + i, index + 1):
                    self._board[x][y] = old_c
                    return True
            self._board[x][y] = old_c
        return False
    

testCases = [
    ([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS"),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.exist(*test)}')
