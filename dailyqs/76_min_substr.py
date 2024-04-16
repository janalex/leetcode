from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        s_counter = Counter(s)
        t_counter = Counter(t)
        for ch, count in t_counter.items():
            if s_counter[ch] < count:
                return ''

        l_index = 0
        for ch in s:
            if t_counter[ch] and s_counter[ch] - 1 < t_counter[ch]:
                break
            s_counter[ch] -= 1
            l_index += 1
        r_index = 0
        for ch in reversed(s):
            if t_counter[ch] and s_counter[ch] - 1 < t_counter[ch]:
                break
            s_counter[ch] -= 1
            r_index += 1
        r_index = len(s) - r_index
        min_len = r_index - l_index
        min_l_index = l_index
        min_r_index = r_index
        last_r_index = r_index

        for i in range(l_index - 1, -1, -1):
            s_counter[s[i]] += 1
            j = 0
            for j in range(last_r_index - 1, i, -1):
                ch = s[j]
                if t_counter[ch] and s_counter[ch] - 1 < t_counter[ch]:
                    break
                s_counter[ch] -= 1
            last_r_index = j + 1
            if last_r_index - i < min_len:
                min_len = last_r_index - i
                min_l_index = i
                min_r_index = last_r_index

        return s[min_l_index:min_r_index]


testCases = [
    ["babcaacabcabbbca", "aaabb"],
    ["ab", "b"],
    ["cabwefgewcwaefgcf", "cae"],
    ("ADOBECODEBANC", "ABC"),
    ("a", "a"),
    ("a", "aa"),
]

s = Solution()
for test in testCases:
    print(f'{test}: \'{s.minWindow(test[0], test[1])}\'')
