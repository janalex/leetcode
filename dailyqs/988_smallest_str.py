from typing import List, Optional, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.min_str: str | None = None
        self.__dfs(root, '')
        return self.min_str if self.min_str else ''

    def __dfs(self, node: TreeNode | None, prefix: str):
        if not node:
            return
        
        prefix = chr(97 + node.val) + prefix
        if not node.left and not node.right:
            if not self.min_str or prefix < self.min_str:
                self.min_str = prefix
        else:
            self.__dfs(node.left, prefix)
            self.__dfs(node.right, prefix)

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

testCases = [
    [0, 1, 2, 3, 4, 3, 4],
    [25, 1, 3, 1, 3, 0, 2],
    [2, 2, 1, None, 1, 0, None, 0, None],
]

s = Solution()
for test in testCases:
    print(f'{test}: "{s.smallestFromLeaf(buildTree(test))}"')
