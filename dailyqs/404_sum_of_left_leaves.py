from collections import deque
from typing import List, Optional, Self


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.__dfs(root, False) if root else 0
    
    def __dfs(self, node : TreeNode, isLeft: bool) -> int:
        result = 0
        if not node.left and not node.right:
            result += node.val if isLeft else 0
        else:
            result += self.__dfs(node.left, True) if node.left else 0
            result += self.__dfs(node.right, False) if node.right else 0

        return result

def buildTree(data: List[int | None]) -> TreeNode | None:
    nodes = deque([TreeNode(x) if x else None for x in data])
    root = nodes.popleft()
    n = root
    index = 0
    while index < len(nodes):
        if n:
            n.left = nodes[index]
            n.right = nodes[index + 1]
        index += 1
        n = nodes.popleft()
    return root


testCases : List[List[int | None]] = [
    [1, 2, None],
    [3, 9, 20, None, None, 15, 7],
    [1],
]

s = Solution()
for test in testCases:
    print(f'{test}: {s.sumOfLeftLeaves(buildTree(test))}')
