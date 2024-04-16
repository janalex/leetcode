from typing import List, Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next: Self | None = None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l2_tail = list2
        while l2_tail.next:
            l2_tail = l2_tail.next

        l1_node = list1
        for i in range(a - 1):
            if l1_node:
                l1_node = l1_node.next

        if not l1_node:
            return list1

        l1_node2 = l1_node.next
        l1_node.next = list2

        for i in range(b - a + 1):
            if l1_node2:
                l1_node2 = l1_node2.next

        l2_tail.next = l1_node2

        return list1


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
    ([10, 1, 13, 6, 9, 5], 3, 4, [1000000, 1000001, 1000002]),
    ([0, 1, 2, 3, 4, 5, 6], 2, 5, [1000000, 1000001, 1000002, 1000003, 1000004]),
]

s = Solution()
for test in testCases:
    print(f'{test}: {listToArray(s.mergeInBetween(buildList(test[0]), test[1], test[2], buildList(test[3])))}')
