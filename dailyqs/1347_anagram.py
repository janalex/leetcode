class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sc = {}
        tc = {}
        for c1, c2 in zip(s, t):
            sc[c1] = sc.get(c1, 0) + 1
            tc[c2] = tc.get(c2, 0) + 1
        toAdd = 0
        for scc in sc.items():
            tcc = tc.get(scc[0], 0)
            if scc[1] > tcc:
                toAdd += scc[1] - tcc
        return toAdd

testCases = [
    ["bab", "aba"],
    ["leetcode", "practice"],
    ["anagram", "mangaar"]
]

for words in testCases:
    s = Solution()
    print(f'{words[0]=} and {words[1]=}: {s.minSteps(words[0], words[1])}')
