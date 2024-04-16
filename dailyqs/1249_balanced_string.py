class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        pars = []
        output = []
        for c in s:
            if c == '(':
                pars.append(len(output))
            elif c == ')':
                if not pars:
                    continue
                pars.pop()
            output.append(c)

        for i in pars:
            output[i] = ''

        return ''.join(output)


testCases = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "))((",
]

s = Solution()
for test in testCases:
    print(f'{test}: "{s.minRemoveToMakeValid(test)}"')
