from collections import Counter, deque
from typing import List, Optional, Self


class TreeNode:
    def __init__(self, val : int = 0, left : Self | None = None, right : Self | None = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        count = 0
        stack = [(root, int(0))]
        while stack:
            node, path = stack.pop()
            if node:
                # alternate 1 and 0 for the digit occurence (0 means even number of occurences)
                path ^= 1 << node.val 
                if not node.left and not node.right: # leaf node
                    if path & (path - 1) == 0: # there can be at most one odd number of occurences
                        count += 1
                else:
                    stack.append((node.left, path))
                    stack.append((node.right, path))
        return count

    def pseudoPalindromicPaths1(self, root: Optional[TreeNode]) -> int:
        result = [0]
        self.dfs(root, '', result)
        return result[0]
    
    def dfs(self, node: TreeNode | None, path: str, result: List[int]):
        if node: 
            path += str(node.val)
            if not node.left and not node.right: # leaf node
                cntr = Counter(path)
                found_odd = False
                for count in cntr.values(): # there can be at most one odd number of occurences
                    if count % 2 == 1:
                        if not found_odd:
                            found_odd = True
                        else:
                            return
                result[0] += 1
            else:
                self.dfs(node.left, path, result)
                self.dfs(node.right, path, result)

def buildTree(data : List[int|None]) -> TreeNode | None:
    nodes = deque([TreeNode(x) if x else None for x in data ])
    root = nodes.popleft()
    n = root
    index = 0
    while index < len(nodes):
        if n:
            n.left = nodes[index]
            n.right = nodes[index+1]
        index += 1
        n = nodes.popleft()
    return root

testCases : List[List[int|None]] = [
    [2,3,1,3,1,None,1],
    [1,2,None,3,None,None,None,4,None],
    [2,1,1,1,3,None,None,None,None,None,1],
    [9]
]
s = Solution()
for test in testCases:
    root = buildTree(test)
    print(f'{test} : {s.pseudoPalindromicPaths1(root)}')