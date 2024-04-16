class Solution:
    def removeKdigits1(self, num: str, k: int) -> str:
        result = []
        number = [int(c) for c in num]

        for i in range(len(number) - 1):
            if number[i] <= number[i + 1]:
                if result or number[i] > 0:
                    result.append(str(number[i]))
            elif k == 0:
                result.append(str(number[i]))
            else:
                k -= 1
        result.append(str(number[-1]))
        while k and result:
            result.pop()
            k -= 1

        if not result:
            return '0'
        return ''.join(result)
    
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            if stack or digit > '0':
                stack.append(digit)

        # If k > 0, remove remaining k digits from the end of the stack
        stack = stack[:-k] if k > 0 else stack

        # Remove leading zeros
        result = ''.join(stack)

        # Handle edge case where result might be empty
        return result if result else '0'
    

testCases = [
    ("10001", 4),
    ("1234567890", 9),
    ("9", 1),
    ("1432219", 3),
    ("10200", 1),
    ("10", 2),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.removeKdigits(*test)}')
