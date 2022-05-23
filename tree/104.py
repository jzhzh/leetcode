# Self-Solution 1
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        res = 0
        depth = 0
        def traverse(root):
            nonlocal depth
            nonlocal res
            if root is None:
                return
            depth += 1
            if (root.left is None) and (root.right is None):
                res = max(res, depth)
            traverse(root.left)
            traverse(root.right)
            depth -= 1
            
        traverse(root)
        return res



# Self-Solution 2
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """ 
        if root is None: 
            return 0
        left_height = self.maxDepth(root.left) 
        right_height = self.maxDepth(root.right) 
        return max(left_height, right_height) + 1 
