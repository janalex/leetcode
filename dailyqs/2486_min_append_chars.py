class Solution:
    def appendCharacters1(self, s: str, t: str) -> int:
        s_i = 0
        for t_i, t_c in enumerate(t):
            while s_i < len(s) and s[s_i] != t_c:
                s_i += 1
            if s_i == len(s):
                break
            s_i += 1
        return len(t) - t_i if s_i == len(s) else 0

    def appendCharacters(self, s: str, t: str) -> int:
        si = ti = 0
        while ti < len(t) and si < len(s):
            if s[si] == t[ti]:
                ti += 1
            si += 1
        return len(t) - ti if si == len(s) else 0

testCases = [
    ("coaching", "coding"),
    ("abcde", "a"),
    ("z", "abcde"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.appendCharacters(*test)}')
