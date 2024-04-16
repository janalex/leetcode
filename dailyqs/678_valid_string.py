class Solution:
    def checkValidString(self, s: str) -> bool:
        stars_count = 0
        pars = []
        for c in s:
            if c == '*':
                stars_count += 1
            elif c == '(':
                pars.append(stars_count)
            else:
                if pars:
                    pars.pop()
                elif stars_count:
                    stars_count -= 1
                else:
                    return False
        
        for count in reversed(pars):
            if stars_count - count <= 0:
                return False
            else:
                stars_count -= 1
        return True
    

testCases = [
    "()(())(((((()())(()))))()(*()))()()()()((()(())())*((((())))*())()(()()))*((()(()(()))))(()())(*(*",
    "****((((((****",
    "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",
    "()",
    "(*)",
    "(*))",
    "*)(",
    "((*())*",
    "*("
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.checkValidString(test)}')
