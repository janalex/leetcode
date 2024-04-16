from typing import List

CAP = 10**9 + 7

class Solution1:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        result = 0
        for i in range(size):
            rowMin = arr[i]
            for j in range(size-i):
                rowMin = min(rowMin, arr[i+j])
                result += rowMin
        return result % CAP

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        size = len(arr)
        result = 0
        unprocessed = []
        for i in range(size + 1):
            while unprocessed and (i == size or arr[i] < arr[unprocessed[-1]]):
                index = unprocessed.pop()
                left = unprocessed[-1] if unprocessed else -1
                count = (index - left) * (i - index)
                result += (count * arr[index]) % CAP
                result %= CAP
            unprocessed.append(i)
        return result

testCases = [
    [3,1,2,4],
    [11,81,94,43,3]
]

s = Solution()
for test in testCases:
    print(f'{s.sumSubarrayMins(test)}')
