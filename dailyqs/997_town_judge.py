from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        not_trusting = {x for x in range(1, n + 1)}
        trust_counts = [0 for _ in range(n+1)]

        for t in trust:
            not_trusting.discard(t[0])
            trust_counts[t[1]] += 1
        
        if len(not_trusting) != 1:
            return -1
        maybe_judge = not_trusting.pop()
        return maybe_judge if trust_counts[maybe_judge] == n - 1 else -1
    

testCases = [
    (2, [[1, 2]]),
    (3, [[1, 3], [2, 3]]),
    (3, [[1, 3], [2, 3], [3, 1]]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findJudge(*test)}')