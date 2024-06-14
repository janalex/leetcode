from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_index = 0
        two_index = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 0 and z_index < i or nums[i] == 2 and two_index > i:
                if nums[i] == 0:
                    if z_index < i:
                        nums[i], nums[z_index] = nums[z_index], nums[i]
                        z_index += 1
                elif nums[i] == 2:
                    if two_index > i:
                        nums[i], nums[two_index] = nums[two_index], nums[i]
                        two_index -= 1


testCases = [
    [0, 0, 0],
    [1, 2, 0],
    [2, 0, 2, 1, 1, 0],
    [2, 0, 1],
]

s = Solution()
for test in testCases:
    print(f'{test}: ', end='')
    s.sortColors(test)
    print(f'{test}')
