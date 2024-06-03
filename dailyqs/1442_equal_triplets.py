from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        sums: list[dict[int, int]] = [{} for _ in range(len(arr))]
        count = 0
        for k in range(len(arr)):
            xor_val = 0
            for j in range(k, -1, -1):
                xor_val ^= arr[j]
                sums[k][xor_val] = sums[k].get(xor_val, 0) + 1
                if j > 0:
                    count += sums[j - 1].get(xor_val, 0)
        return count


testCases = [
    [2, 3, 1, 6, 7],
    [1, 1, 1, 1, 1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.countTriplets(test)}')
