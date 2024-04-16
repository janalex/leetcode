class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return (n and (not (n & (n-1)))) != 0
    
testCases = [
    1,
    16,
    -16,
    3,
    0,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.isPowerOfTwo(test)}')
