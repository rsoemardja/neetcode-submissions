from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th smallest value (1-indexed) in a Binary Search Tree.
        
        Parameters:
        - root (Optional[TreeNode]): The root node of the BST.
        - k (int): The 1-based index of the smallest element to find.
        
        Returns:
        - int: The value of the k-th smallest element.
        """
        stack = []
        current = root
        
        # Traverse the tree iteratively
        while current or stack:
            # Step 1: Reach the leftmost node of the current subtree
            while current:
                stack.append(current)
                current = current.left
            
            # Step 2: Current is now None, so pop the top item from the stack
            current = stack.pop()
            
            # Step 3: Decrement k. If it hits 0, we found our k-th smallest value
            k -= 1
            if k == 0:
                return current.val
            
            # Step 4: We have visited the left side and the root; now check the right subtree
            current = current.right
            
        return -1  # Fallback return statement (guaranteed by constraints to not be hit)