class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = 0
        result = 0
        while numBottles:
            result += numBottles
            empty_bottles += numBottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
        return result


testCases = [
    (9, 3),
    (15, 4),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.numWaterBottles(*test)}')
