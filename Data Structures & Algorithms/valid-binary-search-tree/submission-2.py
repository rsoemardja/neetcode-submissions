from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a given binary tree is a correct Binary Search Tree (BST).
        
        Parameters:
        - root (Optional[TreeNode]): The root node of the binary tree.
        
        Returns:
        - bool: True if the tree is a valid BST, otherwise False.
        """
        
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # Base Case: An empty tree or empty leaf child is always a valid BST
            if not node:
                return True
            
            # The current node's value must stay strictly within the (low, high) bounds
            if not (low < node.val < high):
                return False
            
            # Recursively validate subtrees with updated bounds:
            # - Left child must be smaller than node.val -> update the high limit
            # - Right child must be larger than node.val -> update the low limit
            return (validate(node.left, low, node.val) and 
                    validate(node.right, node.val, high))

        # Start the validation process with unbounded limits (-infinity to +infinity)
        return validate(root, float('-inf'), float('inf'))