from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        q = deque(maxlen=len(deck))
        for card in deck:
            if q:
                first = q.popleft()
                q.append(first)
            q.append(card)
        i = len(deck) - 1
        for card in q:
            deck[i] = card
            i -= 1
        return deck
    

testCases = [
    [17, 13, 11, 2, 3, 5, 7],
    [1, 1000],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.deckRevealedIncreasing(test)}')
