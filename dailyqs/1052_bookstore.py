from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        max_satisfied = 0
        for i in range(len(customers)):
            if i < minutes or not grumpy[i]:
                max_satisfied += customers[i]
        current_satisfied = max_satisfied
        for start in range(0, len(customers) - minutes):
            if grumpy[start]:
                current_satisfied -= customers[start]
            if grumpy[start + minutes]:
                current_satisfied += customers[start + minutes]
            max_satisfied = max(max_satisfied, current_satisfied)
        return max_satisfied


testCases = [
    ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3),
    ([1], [0], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxSatisfied(*test)}')
