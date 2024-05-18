from typing import Optional, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return (0, 0)
            l_coins, l_moves = dfs(node.left)
            r_coins, r_moves = dfs(node.right)
            return (l_coins + r_coins + node.val - 1, l_moves + r_moves + abs(l_coins) + abs(r_coins))
        return dfs(root)[1]


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


testCases: list[list[int | None]] = [
    [3, 0, 0],
    [0, 3, 0],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.distributeCoins(buildTree(test))}')
