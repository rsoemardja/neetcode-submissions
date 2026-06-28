# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # Helper function returns height if balanced, or -1 if unbalanced
        def check_balance(node):
            if not node:
                return 0
            
            # 1. Get height of left subtree
            left_h = check_balance(node.left)
            if left_h == -1: return -1
            
            # 2. Get height of right subtree
            right_h = check_balance(node.right)
            if right_h == -1: return -1
            
            # 3. Check if current node is balanced
            if abs(left_h - right_h) > 1:
                return -1
            
            # 4. If balanced, return the height
            return 1 + max(left_h, right_h)
            
        # If the result is not -1, it's balanced
        return check_balance(root) != -1