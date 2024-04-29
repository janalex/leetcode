from collections import deque
import sys


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        self.ring = ring
        self.r_size = len(ring)
        self.key = key
        self.positions: dict[str, list[int]] = {}
        for i, c in enumerate(ring):
            self.positions.setdefault(c, []).append(i)
        self.memo: dict[tuple[int, int], int] = {}
        return self._dfs(0, 0)

    def _dfs(self, k_index: int, pos: int) -> int:
        if k_index == len(self.key):
            return 0
        if (pos, k_index) in self.memo:
            return self.memo[(pos, k_index)]
        result = sys.maxsize
        for new_pos in self.positions[self.key[k_index]]:
            clicks = abs(new_pos - pos)
            clicks = min(clicks, self.r_size - clicks) + 1
            result = min(result, self._dfs(k_index + 1, new_pos) + clicks)
        self.memo[(pos, k_index)] = result
        return result


testCases = [
    ("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"),
    ("godding", "gd"),
    ("godding", "godding"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findRotateSteps(*test)}')
