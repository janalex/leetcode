from typing import List, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self._dfs(0, root)
        return root
    
    def _dfs(self, from_parent: int, node: TreeNode | None) -> int:
        if not node:
            return from_parent
        node.val += self._dfs(from_parent, node.right)
        if node.left:
            return self._dfs(node.val, node.left)
        else:
            return node.val


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
    return root # type: ignore


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
    [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
    [0, None, 1]
]

s = Solution()
for test in testCases:
    print(f'{test}: {treeToList(s.bstToGst(buildTree(test)))}')
