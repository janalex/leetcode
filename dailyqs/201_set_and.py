import timeit
from typing import List


START = 2 ** 31

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cbit = START
        common_prefix = 0
        while cbit > 0:
            lbit = left & cbit
            if lbit == right & cbit:
                common_prefix += lbit
            else:
                break
            cbit >>= 1
        return common_prefix
    
    def rangeBitwiseAnd2(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1
        return left << count

testCases : List[tuple[int, int]] = [
    (5, 7),
    (0, 0),
    (1, 2147483647),
    (6, 7),
    (20, 2_000_000),
    (10, 10_000_000),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.rangeBitwiseAnd(*test)}')
    print(f'{test}: {s.rangeBitwiseAnd2(*test)}')

def runTest(f, tests):
    for t in tests:
        f(*test)

print(min(timeit.Timer(lambda : runTest(s.rangeBitwiseAnd, testCases)).repeat(7, 100_000)))
print(min(timeit.Timer(lambda: runTest(s.rangeBitwiseAnd2, testCases)).repeat(7, 100_000)))
