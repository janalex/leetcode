class Solution:
    def reverseParentheses(self, s: str) -> str:
        output: list[str] = []
        left_pars: list[int] = []
        for c in s:
            if c == '(':
                left_pars.append(len(output))
            elif c == ')':
                left = left_pars.pop()
                right = len(output) - 1
                while left < right:
                    output[left], output[right] = output[right], output[left]
                    left += 1
                    right -= 1
            else:
                output.append(c)
        return ''.join(output)


testCases = [
    "(abcd)",
    "(u(love)i)",
    "(ed(et(oc))el)",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.reverseParentheses(test)}')
