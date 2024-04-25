class Solution:
    _seeds = [0, 1, 1]

    def tribonacci1(self, n: int) -> int:
        self._results = [-1] * (n + 1)
        return self._trib(n)

    def _trib(self, n: int) -> int:
        if n < 3:
            return Solution._seeds[n]
        if self._results[n] == -1:
            self._results[n] = self._trib(n - 3) + self._trib(n - 2) + self._trib(n - 1)
        return self._results[n]

    def tribonacci(self, n: int) -> int:
        results = [1] * (n + 1)
        results[0] = 0
        for i in range(3, n + 1):
            results[i] = results[i - 3] + results[i - 2] + results[i - 1]
        return results[n]

testCases = [
    4,
    25,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.tribonacci(test)}')
