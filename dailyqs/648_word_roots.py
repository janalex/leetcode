from typing import List, Self


class Trie:
    def __init__(self, value='', is_term=False) -> None:
        self.value = value
        self.is_term = is_term
        self.children: list[Trie | None] = [None] * (ord('z') - ord('a') + 1)

    def is_child(self, char: str) -> bool:
        return self.children[ord(char) - ord('a')] is not None

    def get_child_with_add(self, char: str) -> Self:
        child = self.children[ord(char) - ord('a')]
        if child is None:
            child = Trie(char)
            self.children[ord(char) - ord('a')] = child
        return child  # type: ignore


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root in dictionary:
            node = trie
            for c in root:
                node = node.get_child_with_add(c)
            node.is_term = True

        result = []
        for word in sentence.split():
            node = trie
            right = 0
            found = False
            while right < len(word) and node.is_child(word[right]):
                node = node.get_child_with_add(word[right])
                if node.is_term:
                    found = True
                    break
                right += 1
            if not found:
                result.append(word)
            else:
                result.append(word[:right + 1])
        return ' '.join(result)


testCases = [
    (["cat", "bat", "rat"], "the cattle was rattled by the battery"),
    (["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.replaceWords(*test)}')
