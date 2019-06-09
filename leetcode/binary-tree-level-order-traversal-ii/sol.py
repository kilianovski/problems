# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode):
        result, level = [], [root]
        while root and level:
            result.append([n.val for n in level])
            level = [child for n in level for child in [n.left, n.right] if child]

        result.reverse()
        return result

root = TreeNode(3)

root.left = TreeNode(5)
rightNode = TreeNode(20)
rightNode.left = TreeNode(42)
root.right = rightNode

print(Solution().levelOrderBottom(root))