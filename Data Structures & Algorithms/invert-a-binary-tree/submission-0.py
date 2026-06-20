# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 1. Base Case: If we hit a leaf's child, stop.
        if not root:
            return None
        
        # 2. Action: Swap the left and right children
        # We use Python's simultaneous assignment to do this in one line
        root.left, root.right = root.right, root.left
        
        # 3. Recursion: Go deeper into both branches
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        