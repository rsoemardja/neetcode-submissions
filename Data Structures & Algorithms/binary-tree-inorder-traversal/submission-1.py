# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)    # Left
            result.append(node.val) # Root
            traverse(node.right)   # Right
            
        traverse(root)
        return result