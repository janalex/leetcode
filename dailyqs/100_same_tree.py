# Definition for a binary tree node.

from typing import Optional, Self


class TreeNode:
    def __init__(self, val: int = 0, left: Self|None = None, right: Self|None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        leftNodes = [p]
        rightNodes = [q]
        while leftNodes and rightNodes:
            l = leftNodes.pop()
            r = rightNodes.pop()
            if not l and not r:
                continue
            if not l or not r:
                break
            if l.val != r.val:
                break
            leftNodes.append(l.left)
            leftNodes.append(l.right)
            rightNodes.append(r.left)
            rightNodes.append(r.right)

        return not leftNodes and not rightNodes
