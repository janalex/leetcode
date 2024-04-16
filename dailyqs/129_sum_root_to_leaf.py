from collections import deque
from typing import List, Optional, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        return self.__dfs(root, '') if root else 0

    def __dfs(self, node: TreeNode, prefix: str) -> int:
        prefix = prefix + str(node.val)

        if not node.left and not node.right:
            return int(prefix)

        result = 0
        result += self.__dfs(node.left, prefix) if node.left else 0
        result += self.__dfs(node.right, prefix) if node.right else 0

        return result

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.__dfs1(root, 0) if root else 0

    def __dfs1(self, node: TreeNode, prefix: int) -> int:
        val = 10 * prefix + node.val
        if not node.left and not node.right:
            return val
        result = 0
        result += self.__dfs1(node.left, val) if node.left else 0
        result += self.__dfs1(node.right, val) if node.right else 0
        return result


def buildTree(data: List[int | None]) -> TreeNode | None:
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


testCases: list[list[int | None]] = [
    [4, 9, 0, 5, 1],
    [1, 2, 3],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.sumNumbers(buildTree(test))}')
