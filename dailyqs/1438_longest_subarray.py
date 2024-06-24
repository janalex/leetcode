from sortedcontainers import SortedDict
import heapq
from typing import List


class Solution:
    def longestSubarray(self, nums, limit):
        max_heap = []
        min_heap = []

        left = 0
        max_length = 0
        indexes = []

        for right in range(len(nums)):
            heapq.heappush(max_heap, (-nums[right], right))
            heapq.heappush(min_heap, (nums[right], right))

            # Check if the absolute difference between the maximum and minimum values
            # in the current window exceeds the limit
            while -max_heap[0][0] - min_heap[0][0] > limit:
                # Move the left pointer to the right until the condition is satisfied.
                # This ensures we remove the element causing the violation
                left = min(max_heap[0][1], min_heap[0][1]) + 1

                # Remove elements from the heaps that are outside the current window
                while max_heap[0][1] < left:
                    heapq.heappop(max_heap)
                while min_heap[0][1] < left:
                    heapq.heappop(min_heap)

            # Update max_length with the length of the current valid window
            if max_length < right - left + 1:
                max_length = right - left + 1
                indexes = [left, right]

        return [max_length, indexes]

    def longestSubarray1(self, nums: List[int], limit: int) -> list:
        max_len = 1
        indexes = [0, 0]
        asc_heap: list[tuple[int, int]] = [(nums[0], 0)]
        desc_heap: list[tuple[int, int]] = [(-nums[0], 0)]
        start = 0
        for i in range(1, len(nums)):
            if nums[i] < asc_heap[0][0]:
                if -desc_heap[0][0] - nums[i] > limit:
                    # asc_heap = []
                    min_index = 0
                    new_desc_heap = []
                    while desc_heap and -desc_heap[0][0] - nums[i] > limit:
                        _, index = heapq.heappop(desc_heap)
                        min_index = max(min_index, index)
                    for value, index in desc_heap:
                        if index > min_index:
                            heapq.heappush(new_desc_heap, (value, index))
                    desc_heap = new_desc_heap
                    start = desc_heap[0][1] if desc_heap else i
            elif nums[i] > -desc_heap[0][0]:
                if nums[i] - asc_heap[0][0] > limit:
                    # desc_heap = []
                    new_asc_heap = []
                    min_index = 0
                    while asc_heap and nums[i] - asc_heap[0][0] > limit:
                        _, index = heapq.heappop(asc_heap)
                        min_index = max(min_index, index)
                    for value, index in asc_heap:
                        if index > min_index:
                            heapq.heappush(new_asc_heap, (value, index))
                    asc_heap = new_asc_heap
                    start = asc_heap[0][1] if asc_heap else i
            heapq.heappush(asc_heap, (nums[i], i))
            heapq.heappush(desc_heap, (-nums[i], i))
            if max_len < i - start + 1:
                max_len = i - start + 1
                indexes = [start, i]
        return [max_len, indexes]

    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        # SortedDict to maintain the elements within the current window
        window = SortedDict()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1

            # Check if the absolute difference between the maximum and minimum values
            # in the current window exceed the limit
            while window.peekitem(-1)[0] - window.peekitem(0)[0] > limit: # type: ignore
                # Remove the element at the left pointer from the SortedDict
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                # Move the left pointer to the right to exclude the element causing the violation
                left += 1

            # Update maxLength with the length of the current valid window
            max_length = max(max_length, right - left + 1)

        return max_length

testCases = [
    ([24, 12, 71, 33, 5, 87, 10, 11, 3, 58, 2, 97, 97, 36, 32, 35, 15, 80, 24,
      45, 38, 9, 22, 21, 33, 68, 22, 85, 35, 83, 92, 38, 59, 90, 42, 64, 61, 15,
      4, 40,50, 44, 54, 25, 34, 14, 33, 94, 66, 27, 78, 56, 3, 29, 3, 51, 19, 5,
      93, 21, 58, 91, 65, 87, 55, 70, 29, 81, 89, 67, 58, 29, 68, 84, 4, 51, 87,
      74, 42, 85, 81, 55, 8, 95, 39], 87),
    ([8], 10),
    ([2, 5, 2], 9),
    ([4, 2, 2, 2, 4, 4, 2, 2], 0),
    ([8, 2, 4, 7], 4),
    ([10, 1, 2, 4, 7, 2], 5),
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.longestSubarray2(*test)}')
