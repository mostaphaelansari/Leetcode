from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        q = deque([root])
        
        while q:
            size = len(q)
            foundX = foundY = False
            
            for _ in range(size):
                node = q.popleft()
                
                if node.val == x:
                    foundX = True
                if node.val == y:
                    foundY = True

                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                       (node.left.val == y and node.right.val == x):
                        return False

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if foundX and foundY:
                return True
            if foundX or foundY:
                return False
        
        return False
