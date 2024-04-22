from collections import deque
from typing import List

mults = [1, 10, 100, 1000]
positions = [
    [9, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
]

class Solution:
    def openLock1(self, deadends: List[str], target: str) -> int:
        visited = {}
        result = 0
        q: deque[tuple[str, int]] = deque([('0000', 0)])
        found = False
        while q:
            code, count = q.popleft()
            if visited.get(code):
                continue
            visited[code] = True
            if code in deadends:
                continue
            if code == target:
                found = True
                result = count
                break
            new_code = list(code)
            for i in range(4):
                d = int(code[i])
                for shift in [-1, 1]:
                    new_code[i] = str(abs((d + shift) % 10))
                    q.append((''.join(new_code), count + 1))
                new_code[i] = code[i]
        return result if found else -1

    def openLock(self, deadends: List[str], target: str) -> int:
        black_list = set([int(x) for x in deadends])
        visited = {}
        result = 0
        goal = int(target)
        q: deque[tuple[int, int]] = deque([(0, 0)])
        found = False
        while q:
            code, count = q.popleft()
            if visited.get(code):
                continue
            visited[code] = True
            if code in black_list:
                continue
            if code == goal:
                found = True
                result = count
                break
            c = code
            for i in range(4):
                d = c % 10
                c //= 10
                for shift in range(2):
                    d_new = positions[shift][d]
                    q.append((code + (d_new - d) * mults[i], count + 1))
        return result if found else -1


testCases = [
    (["0201", "0101", "0102", "1212", "2002"], "0202"),
    (["8888"], "0009"),
    (["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.openLock(*test)}')
