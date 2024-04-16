from dataclasses import dataclass
from typing import List, Set

@dataclass
class Word:
    word: Set[str]
    is_valid: bool

class Solution:
    input: List[Word]

    def maxLength(self, arr: List[str]) -> int:
        self.input = []
        for w in arr:
            ws = set(w)
            valid = len(ws) == len(w)
            self.input.append(Word(ws, valid))

        return self.maxLength1(set(), 0, 0)
    
    def maxLength1(self, letters: Set[str], startIndex: int, length: int) -> int:
        if startIndex == len(self.input):
            return length

        maxLength = length        
        for index in range(startIndex, len(self.input)):
            if not self.input[index].is_valid:
                continue
            word = self.input[index].word
            if letters & word:
                continue

            letters.update(word)
            l = length + len(word)
            localMax = l
            for i in range(index + 1, len(self.input)):
                l1 = self.maxLength1(letters, i, l)
                localMax = max(localMax, l1)
            letters.difference_update(word)
            maxLength = max(maxLength, localMax)

        return maxLength

testCases = [
    ["zog","nvwsuikgndmfexxgjtkb","nxko"],
    ["un","iq","ue"],
    ["cha","r","act","ers"],
    ["abcdefghijklmnopqrstuvwxyz"],
    ['aa', 'bb'],
    ["a", "abc", "d", "de", "def"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxLength(test)}')
