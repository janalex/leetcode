from typing import List


class Solution:
    def countStudents1(self, students: List[int], sandwiches: List[int]) -> int:
        left = len(sandwiches) + 1
        sandwiches.reverse()
        while sandwiches and left > len(sandwiches):
            left = len(sandwiches)
            for i, s in enumerate(students):
                if s > -1:
                    if s == sandwiches[-1]:
                        sandwiches.pop()
                        students[i] = -1
        return len(sandwiches)

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s_freq = [0, 0]
        for st in students:
            s_freq[st] += 1

        result = len(sandwiches)
        for s in sandwiches:
            if s_freq[s] > 0:
                s_freq[s] -= 1
                result -= 1
            else:
                break

        return result

testCases = [
    ([1, 1, 0, 0], [0, 1, 0, 1]),
    ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countStudents(*test)}')
