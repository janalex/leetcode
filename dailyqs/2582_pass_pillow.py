class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        passes = time // (n - 1)
        remainder = time % (n - 1)
        if passes % 2:
            return n - remainder
        else:
            return remainder + 1


testCases = [
    (4, 5),
    (3, 2),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.passThePillow(*test)}')
