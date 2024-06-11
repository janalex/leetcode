from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001
        for num in arr1:
            counts[num] += 1
        result = []
        for num in arr2:
            for _ in range(counts[num]):
                result.append(num)
            counts[num] = 0
        for i in range(1001):
            if counts[i]:
                for _ in range(counts[i]):
                    result.append(i)
        return result


testCases = [
    ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
    ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.relativeSortArray(*test)}')
