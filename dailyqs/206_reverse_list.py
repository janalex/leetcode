from typing import List, Optional, Self

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev


def buildList(arr: List[int]) -> ListNode | None:
    if not arr:
        return None

    head = ListNode()
    node = head
    prev = None
    for i in arr:
        node.val = i
        if prev:
            prev.next = node
        prev = node
        node = ListNode()
    return head


def listToArray(node: ListNode | None) -> List[int] | None:
    if not node:
        return None
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


testCases = [
    [1, 2, 3, 4, 5],
    [1, 2],
    [1],
    [],
]

s = Solution()
for test in testCases:
    print(f'{test}: {listToArray(s.reverseList(buildList(test)))}')
