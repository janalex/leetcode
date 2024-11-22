from typing import List


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        asc_positions = [(pos, i) for i, pos in enumerate(positions)]
        asc_positions.sort()
        stack = []
        for _, robot in asc_positions:
            dir, health = directions[robot], healths[robot]
            died = False
            if dir == 'L':
                while not died and stack and stack[-1][0] == 'R':
                    other_health = stack[-1][1]
                    if health > other_health:
                        health -= 1
                        stack.pop()
                    elif health == other_health:
                        stack.pop()
                        died = True
                    else:
                        stack[-1][1] -= 1
                        died = True
            if not died:
                stack.append([dir, health, robot])
        stack.sort(key=lambda item: item[2])
        return [health for _, health, _ in stack]


testCases = [
    ([3, 5, 2, 6], [10, 10, 15, 12], "RLRL"),
    ([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR"),
    ([1, 2, 5, 6], [10, 10, 11, 11], "RLRL"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.survivedRobotsHealths(*test)}')
