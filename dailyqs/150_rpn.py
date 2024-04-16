import math
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case '+':
                    o1, o2 = stack.pop(), stack.pop()
                    stack.append(o1 + o2)
                case '-':
                    o1, o2 = stack.pop(), stack.pop()
                    stack.append(o2 - o1)
                case '*':
                    o1, o2 = stack.pop(), stack.pop()
                    stack.append(o1 * o2)
                case '/':
                    o1, o2 = stack.pop(), stack.pop()
                    stack.append(math.trunc(o2 / o1))
                case _:
                    stack.append(int(token))
        return stack.pop()
    
testCases = [
    ["4","3","-"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
    ["4","13","5","/","+"],
    ["2","1","+","3","*"],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.evalRPN(test)}')
