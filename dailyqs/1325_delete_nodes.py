from typing import Optional, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.val == target and root.left is None and root.right is None:
            return None
        return root


def buildTree(data: list[int | None]) -> TreeNode | None:
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
    return root


def treeToList(root: TreeNode | None) -> list[int | None]:
    if not root:
        return [None]
    index = 0
    result: list[int | None] = []
    queue: list[TreeNode | None] = [root]
    while index < len(queue):
        node = queue[index]
        result.append(node.val if node else None)
        if node and (node.left or node.right):
            queue.append(node.left)
            queue.append(node.right)
        index += 1
    return result


testCases = [
    ([1, 2, 3, 2, None, 2, 4], 2),
    ([1, 3, 3, 3, 2], 3),
    ([1, 2, None, 2, None, 2], 2),
]

s = Solution()
for test in testCases:
    print(f'{test}: {treeToList(s.removeLeafNodes(buildTree(test[0]), test[1]))}')
