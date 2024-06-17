import math


class Solution:
    def judgeSquareSum1(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            b = c - i * i
            if self._binary_search(0, b, b):
                return True
            i += 1
        return False

    def _binary_search(self, s: int, e: int, n: int) -> bool:
        if s > e:
            return False
        mid = s + (e - s) // 2
        if mid * mid == n:
            return True
        if mid * mid > n:
            return self._binary_search(s, mid - 1, n)
        else:
            return self._binary_search(mid + 1, e, n)

    def judgeSquareSum2(self, c: int) -> bool:
        i = 0
        while i * i <= c:
            b = math.sqrt(c - i * i)
            if b == int(b):
                return True
            i += 1
        return False

    def judgeSquareSum(self, c: int) -> bool:
        for i in range(2, int(math.sqrt(c)) + 1):
            count = 0
            if c % i == 0:
                while c % i == 0:
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
        return c % 4 != 3


testCases = [
    5, 3, 0, 6, 7,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.judgeSquareSum(test)}')
