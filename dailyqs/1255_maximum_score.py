from collections import Counter
from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        cnt = Counter(letters)

        def recurse(index: int, freq: Counter) -> int:
            if index == len(words):
                return 0
            not_taken_score = recurse(index + 1, freq)
            taken_score = 0
            can_take = True
            new_freq = freq.copy()
            for c in words[index]:
                if not new_freq.get(c, 0):
                    can_take = False
                    break
                else:
                    new_freq[c] -= 1
                    s_index = ord(c) - ord('a')
                    taken_score += score[s_index]
            if can_take:
                taken_score += recurse(index + 1, new_freq)
            else:
                taken_score = 0
            return max(not_taken_score, taken_score)

        return recurse(0, cnt)


testCases = [
    (["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"],
     [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    (["xxxz", "ax", "bx", "cx"], ["z", "a", "b", "c", "x", "x", "x"],
     [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]),
    (["leetcode"], ["l", "e", "t", "c", "o", "d"],
     [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxScoreWords(*test)}')
