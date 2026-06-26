# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            
            # Recursive calls to get the height of subtrees
            left = depth(node.left)
            right = depth(node.right)
            
            # Update the global diameter if this node's path is longer
            self.diameter = max(self.diameter, left + right)
            
            # Return height to the parent
            return 1 + max(left, right)
        
        depth(root)
        return self.diameter