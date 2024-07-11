from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        result = 0
        for op in logs:
            if op == './':
                continue
            elif op == '../':
                result = max(0, result - 1)
            else:
                result += 1
        return result


testCases = [
    ["d1/", "d2/", "../", "d21/", "./"],
    ["d1/", "d2/", "./", "d3/", "../", "d31/"],
    ["d1/", "../", "../", "../"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.minOperations(test)}')
