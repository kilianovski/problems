

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode):
        result = []
        q = deque()
        inner_q = deque()
        inner_q.append(root)
        q.append(inner_q)

        while q:
            inner_q = q.popleft()

            if not inner_q:
                break

            new_inner_q = deque()
            this_level_result = []
            while inner_q:
                node = inner_q.popleft()
                if node == None:
                    continue
                this_level_result.append(node.val)
                new_inner_q.append(node.left)
                new_inner_q.append(node.right)

            q.append(new_inner_q)
            if len(this_level_result) != 0:
                result.append(this_level_result)

        return result

root = TreeNode(3)

root.left = TreeNode(5)
rightNode = TreeNode(20)
rightNode.left = TreeNode(42)
root.right = rightNode

print(Solution().levelOrder(root))