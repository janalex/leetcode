from typing import List, Optional, Self

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return

        fast, slow = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next  # pyright: ignore[reportOptionalMemberAccess]

        if fast:  # odd number of nodes
            tail_reverse = slow.next  # pyright: ignore[reportOptionalMemberAccess]
            slow.next = None  # pyright: ignore[reportOptionalMemberAccess]
        else:  # even number of nodes
            tail_reverse = slow
            prev.next = None  # pyright: ignore[reportOptionalMemberAccess]

        prev = None
        while tail_reverse:
            next_node = tail_reverse.next
            tail_reverse.next = prev
            prev = tail_reverse
            tail_reverse = next_node
        reverse_head = prev

        while head and reverse_head:
            next_head = head.next
            next_reverse = reverse_head.next
            head.next = reverse_head
            reverse_head.next = next_head
            reverse_head = next_reverse
            head = next_head


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
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [],
    [1],
    [1, 2],
]

s = Solution()
for test in testCases:
    t = buildList(test)
    s.reorderList(t)
    print(f'{test}: {listToArray(t)}')
