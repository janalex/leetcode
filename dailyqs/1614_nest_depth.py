class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
                result = max(result, depth)
            elif c == ')':
                depth -= 1
        return result
    

testCases = [
    "(1+(2*3)+((8)/4))+1",
    "(1)+((2))+(((3)))",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.maxDepth(test)}')
