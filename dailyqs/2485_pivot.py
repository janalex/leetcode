class Solution:
    def pivotInteger(self, n: int) -> int:
        ps = 0
        total = (n + 1) * n // 2
        p = 1
        while p <= n:
            remain = total - ps
            ps += p
            if ps == remain:
                return p
            elif ps > remain:
                return -1
            p += 1

        return -1
    

testCases = [
    8, 1, 4,
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.pivotInteger(test)}')
