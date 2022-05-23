# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def maxDepth(node):
            if not node:
                return 0
            nonlocal max_diameter
            left_depth = maxDepth(node.left)
            right_depth = maxDepth(node.right)
            diameter = left_depth + right_depth
            max_diameter = max(max_diameter, diameter)
            return max(left_depth, right_depth) + 1
        maxDepth(root)
        return max_diameter