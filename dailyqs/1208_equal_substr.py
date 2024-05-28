class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = r = 0
        max_size = 0
        cur_cost = 0
        while r < len(s):
            while r < len(s) and cur_cost + abs(ord(s[r]) - ord(t[r])) <= maxCost:
                cur_cost += abs(ord(s[r]) - ord(t[r]))
                r += 1
            max_size = max(max_size, r - l)
            if r == len(s):
                break
            cur_cost += abs(ord(s[r]) - ord(t[r]))
            r += 1
            # skip the right character completely if the cost of changing just that character
            # is higher than the maxCost
            if abs(ord(s[r - 1]) - ord(t[r - 1])) > maxCost:
                l = r
                cur_cost = 0
                continue
            while cur_cost > maxCost:
                cur_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
        return max_size


testCases = [
    ("abcd", "bcdf", 3),
    ("abcd", "cdef", 3),
    ("abcd", "acde", 0),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.equalSubstring(*test)}')
