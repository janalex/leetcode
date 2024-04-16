class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        l1 = {}
        l2 = {}
        if len(word1) != len(word2):
            return False
        for c1, c2 in zip(word1, word2):
            l1[c1] = l1.get(c1, 0) + 1
            l2[c2] = l2.get(c2, 0) + 1
        
        # both words must have the same set of letters
        for c in l1.keys():
            if c not in l2:
                return False

        occs1 = sorted(l1.values())
        occs2 = sorted(l2.values())
        return occs1 == occs2
    
testCases = [
    ["abc", "bca"],
    ["a", "aa"],
    ["cabbba", "abbccc"],
    ["asa", "ssx"]
]

for words in testCases:
    s = Solution()
    print(f'{words[0]=} and {words[1]=}: {s.closeStrings(words[0], words[1])}')
