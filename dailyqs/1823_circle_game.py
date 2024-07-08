class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [x for x in range(n)]
        start = 0
        while n > 1:
            end = start + k - 1
            pos = end % n
            del players[pos]
            n -= 1
            start = pos % n
        return players[0] + 1

    def findTheWinner1(self, n: int, k: int) -> int:
        ans = 0
        for i in range(2, n + 1):
            ans = (ans + k) % i
        return ans + 1

testCases = [
    (5, 2),
    (6, 5),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.findTheWinner1(*test)}')
