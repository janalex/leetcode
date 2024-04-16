from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            is_palindrome = True
            for i in range(len(w) // 2):
                if w[i] != w[-i - 1]:
                    is_palindrome = False
                    break
            if is_palindrome:
                return w
        return ''
    
    def firstPalindrome2(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ''
    

testCases = [
    ["abc","car","ada","racecar","cool"],
    ["notapalindrome","racecar"],
    ["def","ghi"],
]

s = Solution()
for test in testCases:
    print(f'{test}: \'{s.firstPalindrome(test)}\'')
    print(f'{test}: \'{s.firstPalindrome2(test)}\'')
