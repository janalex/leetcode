from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not len(words):
            return []
        present_chars = self._process_word(words[0], None)
        for i in range(1, len(words)):
            present_chars = self._process_word(words[i], present_chars)
        return [c for c, _ in present_chars]

    def _process_word(self, word: str, existing: set[tuple[str, int]] | None) -> set[tuple[str, int]]:
        chars = {}
        result = set()
        for c in word:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
            char = (c, chars[c])
            if existing != None:
                if char in existing:
                    result.add(char)
            else:
                result.add(char)
        return result


testCases = [
    ["acabcddd", "bcbdbcbd", "baddbadb", "cbdddcac", "aacbcccd", "ccccddda", "cababaab", "addcaccd"],
    ["bella", "label", "roller"],
    ["cool", "lock", "cook"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.commonChars(test)}')
