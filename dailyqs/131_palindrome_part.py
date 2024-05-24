from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        size = len(s)
        dp: dict[tuple[int, int], bool] = {(x, x): True for x in range(size)}
        result: list[list[str]] = []

        def helper(cur_part: list[str], index: int):
            if index == size:
                result.append(cur_part)
            for i in range(index, size):
                if (index, i) in dp:
                    if dp[(index, i)]:
                        new_part = cur_part.copy()
                        new_part.append(s[index:i + 1])
                        helper(new_part, i + 1)
                else:
                    is_palindrome = True
                    start, end = index, i
                    while end >= start:
                        if s[end] != s[start]:
                            is_palindrome = False
                            break
                        start += 1
                        end -= 1
                    dp[(index, i)] = is_palindrome
                    if is_palindrome:
                        new_part = cur_part.copy()
                        new_part.append(s[index:i + 1])
                        helper(new_part, i + 1)

        helper([], 0)
        return result


testCases = [
    "aab",
    "a",
    "abbaa",
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.partition(test)}')
