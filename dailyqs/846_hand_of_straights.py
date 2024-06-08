from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        size = len(hand)
        if size % groupSize:
            return False

        hand.sort()
        cards = [[x, True] for x in hand]
        index = next = 0
        while next < size:
            count = 1
            index = next
            next = 0
            value = cards[index][0]
            cards[index][1] = False
            index += 1
            while count < groupSize:
                while index < size and (cards[index][0] == value or not cards[index][1]):
                    if cards[index][1] and not next:
                        next = index
                    index += 1
                if index == size or cards[index][0] > value + 1:
                    return False
                value = value + 1
                count += 1
                cards[index][1] = False
                index += 1
            if not next:
                next = index
        return True


testCases = [
    ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3),
    ([1, 2, 3, 4, 5], 4),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.isNStraightHand(*test)}')
