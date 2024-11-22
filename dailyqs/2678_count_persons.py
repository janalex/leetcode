from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for detail in details:
            if detail[11] > '6' or detail[11] == '6' and detail[12] > '0':
                count += 1
        return count


testCases = [
    ["7868190130M7522", "5303914400F9211", "9273338290F4010"],
    ["1313579440F2036", "2921522980M5644"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countSeniors(test)}')
