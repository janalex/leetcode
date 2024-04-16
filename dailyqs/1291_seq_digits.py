from typing import List

DIGIT_COUNT: List[int] = [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000]

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result : List[int] = []
        low_digits = self.digitCount(low)
        high_digits = self.digitCount(high)

        for digit_count in range(low_digits, high_digits + 1):
            for start_digit in range(1, 11 - digit_count):
                digit = start_digit
                num = 0
                for _ in range(digit_count):
                    num = num * 10 + digit
                    digit += 1
                if num >= low and num <= high:
                    result.append(num)
        return result

    def digitCount(self, num: int) -> int:
        result = 1
        if num >= DIGIT_COUNT[-1]:
            result = 9
        else:
            while num >= DIGIT_COUNT[result]:
                result += 1
        return result
       
    
testCases = [
    (10, 1000000000),
    (100, 300),
    (1_000, 13_000),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.sequentialDigits(test[0], test[1])}')
