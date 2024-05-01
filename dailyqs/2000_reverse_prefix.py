class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pos = word.find(ch) + 1
        if not pos:
            return word
        prefix = list(word[:pos])
        # prefix.reverse()
        i, j = 0, len(prefix) - 1
        while i < j:
            prefix[i], prefix[j] = prefix[j], prefix[i]
            i += 1
            j -= 1
        prefix.append(word[pos:])
        return "".join(prefix)


testCases = [
    ("abcdefd", "d"),
    ("xyxzxe", "z"),
    ("abcd", "z"),
]

s = Solution()
for test in testCases:
    print(f"{test}: {s.reversePrefix(*test)}")
