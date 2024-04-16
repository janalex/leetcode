from typing import Dict, List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups : Dict[str, list[str]] = {}
        for i, s in enumerate(strs):
            ss = ''.join(sorted(s))
            gv = groups.get(ss)
            if gv:
                gv.append(s)
            else:
                groups[ss] = [s]

        return list(groups.values())
    
testCases = [
    ["eat","tea","tan","ate","nat","bat"],
    [""],
    ["a"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.groupAnagrams(test)}')
