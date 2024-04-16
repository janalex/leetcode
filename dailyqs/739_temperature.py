from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                el = stack.pop()
                result[el[1]] = i - el[1]
            stack.append((t, i))
            result.append(0)
        return result
    
testCases = [
    [73,74,75,71,69,72,76,73],
    [30,40,50,60],
    [30,60,90],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.dailyTemperatures(test)}')
