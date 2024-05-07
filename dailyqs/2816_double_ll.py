from typing import Optional, Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = dummy = ListNode()
        node = head
        while node:
            n = node.next
            node.next = prev
            prev = node
            node = n
        top : ListNode = prev
        carry = 0
        next = None
        while top != dummy:
            n = top.next
            top.val = top.val + top.val + carry
            carry = top.val // 10
            top.val %= 10
            top.next = next
            next = top
            top = n  # pyright: ignore[reportAssignmentType]
        if carry:
            top.val = 1  # pyright: ignore[reportOptionalMemberAccess]
            top.next = next  # pyright: ignore[reportOptionalMemberAccess]
        else:
            top = next  # pyright: ignore[reportAssignmentType]
        return top


def list2node(data: list[int]) -> ListNode | None:
    head = prev = ListNode()
    for val in data:
        node = ListNode(val)
        prev.next = node
        prev = node
    return head.next


def node2list(node: ListNode | None) -> list[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


testCases = [
    [1, 8, 9],
    [9, 9, 9],
]

s = Solution()
for test in testCases:
    print(f'{test}: {node2list(s.doubleIt(list2node(test)))}')
