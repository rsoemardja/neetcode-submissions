# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Base case: if the tree is empty, depth is 0
        if not root:
            return 0
        
        # Recursive step: 
        # 1. Get max depth of left subtree
        # 2. Get max depth of right subtree
        # 3. Take the max of those two and add 1 for the current node
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))