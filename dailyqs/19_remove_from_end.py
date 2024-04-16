from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        prev = head
        node = head.next
        i = 0
        while i < n and node:
            node = node.next
            i += 1
        if i < n:
            return prev.next

        curr = prev.next
        while node:
            prev = curr
            curr = curr.next  # pyright: ignore[reportOptionalMemberAccess]
            node = node.next
        prev.next = curr.next  # pyright: ignore[reportOptionalMemberAccess]
        return head


def buildList(arr: List[int]) -> ListNode:
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
    ([1, 2, 3, 4, 5], 2),
    ([1], 1),
    ([1, 2], 1),
]

s = Solution()
for test in testCases:
    print(f'{test}: {listToArray(s.removeNthFromEnd(buildList(test[0]), test[1]))}')
