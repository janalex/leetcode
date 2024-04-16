from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if depth == 1:
            return TreeNode(val, root)

        nodes = self.getNodesAtDepth(root, depth)
        for node in nodes:
            node.left = TreeNode(val, node.left)
            node.right = TreeNode(val, None, node.right)

        return root

    def getNodesAtDepth(self, node: TreeNode, depth: int) -> list[TreeNode]:
        depth -= 1
        if depth < 2:
            return [node]
        result = []
        if node.left:
            result.extend(self.getNodesAtDepth(node.left, depth))
        if node.right:
            result.extend(self.getNodesAtDepth(node.right, depth))
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

testCases: list[tuple[list[int | None], int, int]] = [
    ([4, 2, 6, 3, 1, 5, None], 1, 2),
    ([4, 2, None, 3, 1], 1, 3),
]

s = Solution()
for test in testCases:
    print(f'{test}: {treeToList(s.addOneRow(buildTree(test[0]), test[1], test[2]))}')
