from typing import List, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_values = []
        self._in_order_traverse(root, sorted_values)
        return self._build_bst1(sorted_values, len(sorted_values) // 2, 0, len(sorted_values) - 1)  # type: ignore

    def _in_order_traverse(self, node: TreeNode | None, result: list[int]) -> None:
        if not node:
            return
        self._in_order_traverse(node.left, result)
        result.append(node.val)
        self._in_order_traverse(node.right, result)

    def _build_bst(self, values: list[int], index: int, left: int, right: int) -> TreeNode:
        node = TreeNode(values[index])
        left_mid = (index + left) // 2
        right_mid = (right + index) // 2
        if right_mid == index:
            right_mid += 1
        if index == left:
            node.left = None
        else:
            node.left = self._build_bst(values, left_mid, left, index)
        if right_mid == right:
            node.right = None
        else:
            node.right = self._build_bst(values, right_mid, index + 1, right)
        return node

    def _build_bst1(self, values: list[int], index: int, left: int, right: int) -> TreeNode | None:
        if right < left:
            return None
        node = TreeNode(values[index])
        left_mid = (index + left) // 2
        right_mid = (index + right) // 2 + 1
        node.left = self._build_bst1(values, left_mid, left, index - 1)
        node.right = self._build_bst1(values, right_mid, index + 1, right)
        return node


def buildTree(data: List[int | None]) -> TreeNode:
    nodes = [TreeNode(x) if x is not None else None for x in data]
    n_index = 0
    root = n = nodes[n_index]
    ch_index = 1
    while ch_index < len(nodes):
        if n:
            n.left = nodes[ch_index]
            n.right = nodes[ch_index + 1]
        ch_index += 2
        n_index += 1
        n = nodes[n_index]
    return root  # type: ignore


def treeToList(root: TreeNode | None) -> list[int | None]:
    if not root:
        return [None]
    index = 0
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while index < len(queue):
        node = queue[index]
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
        index += 1
    return result


testCases = [
    [1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4],
    [2, 1, 3],
]

s = Solution()
for test in testCases:
    print(f'{test}: {treeToList(s.balanceBST(buildTree(test)))}')
