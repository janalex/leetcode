from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not len(tokens):
            return 0

        tokens.sort()
        score = 0
        low = 0
        high = len(tokens) - 1
        while low < high:
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1
            elif score > 0:
                score -= 1
                power += tokens[high]
                high -= 1
            else:
                break

        if tokens[low] <= power:
            score += 1

        return score


testCases = [
    ([100], 50),
    ([200, 100], 150),
    ([100, 200, 300, 400], 200),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.bagOfTokensScore(*test)}')
