from typing import List, Optional, Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            next_slow = slow.next  # pyright: ignore[reportOptionalMemberAccess]
            slow.next = prev  # pyright: ignore[reportOptionalMemberAccess]
            prev = slow
            slow = next_slow

        if fast:
            # odd number of elements in the list
            slow = slow.next  # pyright: ignore[reportOptionalMemberAccess]

        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        
        return True
    

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
    [1, 2, 2, 1],
    [1, 2, 1],
    [1, 2, 3],
    [1, 2],
    [1, 1],
    [1],
    [],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.isPalindrome(buildList(test))}')
