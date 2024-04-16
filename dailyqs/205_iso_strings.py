class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapped_c: dict[str, str] = {}
        is_mapped: set[str] = set()
        for i in range(len(s)):
            c = mapped_c.get(s[i], None)
            if c and t[i] == c:
                continue
            elif not c:
                if t[i] in is_mapped:
                    return False
                is_mapped.add(t[i])
                mapped_c[s[i]] = t[i]
            else:
                return False
        return True


testCases = [
    ("egg", "add"),
    ("foo", "bar"),
    ("paper", "title")
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.isIsomorphic(*test)}')
