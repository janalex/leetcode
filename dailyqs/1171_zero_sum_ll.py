# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional, Self


class ListNode:
    def __init__(self, val : int = 0, next : Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def __delete_nodes(self, start : ListNode | None, end : ListNode, start_sum : int, sums : dict[int, ListNode]):
        while start and start != end:
            start_sum += start.val
            del sums[start_sum]
            start = start.next

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ps: dict[int, ListNode] = {}
        s = 0
        cur = head
        while cur:
            s += cur.val
            if ps.get(s):
                start = ps[s]
                self.__delete_nodes(start.next, cur, s, ps)
                start.next = cur.next
            elif s == 0:
                self.__delete_nodes(head, cur, 0, ps)
                head = cur.next
            else:
                ps[s] = cur

            cur = cur.next

        return head if s != 0 else None


def buildList(data: list[int]) -> ListNode:
    root = cur = ListNode()
    prev = None
    for v in data:
        if prev:
            prev.next = cur
        cur.val = v
        prev = cur
        cur = ListNode()
    return root


def listToArr(l: ListNode | None) -> list[int]:
    arr = []
    while l:
        arr.append(l.val)
        l = l.next
    return arr


testCases = [
    [1, 3, 2, -3, -2, 5, 5, -5, 1],
    [10, -10],
    [1, 2, -3, 3, 1],
    [1, 2, 3, -3, 4],
    [1, 2, 3, -3, -2],
    [-40, 40, 9, -2, 4],
    [24, 38, -38, -6, 19],
]

s = Solution()
for test in testCases:
    print(f'{test}: {listToArr(s.removeZeroSumSublists(buildList(test)))}')
