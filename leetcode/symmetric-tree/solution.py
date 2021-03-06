# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:

    
    def isMirrorTree(self, a: TreeNode, b: TreeNode) -> bool:
        q = deque()

        q.append((a, b))
        

        while q:
            first, second = q.popleft()

            if (first == None and second != None) or (first != None and second == None):
                return False
            if first == None:
                continue

            if first.val != second.val:
                return False

            left = first.left, second.right
            right = first.right, second.left
            q.append(left)
            q.append(right)

        return True
    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or self.isMirrorTree(root.left, root.right)