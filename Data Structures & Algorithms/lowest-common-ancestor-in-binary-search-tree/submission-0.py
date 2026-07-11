# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Finds the lowest common ancestor of two distinct nodes in a given BST.
        
        Parameters:
        - root (TreeNode): The entry point/root node of the Binary Search Tree.
        - p (TreeNode): The first target node.
        - q (TreeNode): The second target node.
        
        Returns:
        - TreeNode: The node representing the lowest common ancestor.
        """
        # Start our tracking pointer at the top of the tree
        curr = root
        
        # Traverse down the tree using the BST properties
        while curr:
            # If both target values are greater than the current node's value,
            # then both targets must reside entirely within the right subtree.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # If both target values are less than the current node's value,
            # then both targets must reside entirely within the left subtree.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # A split has occurred! This means:
            # - One node is to the left and one is to the right, OR
            # - The current node is exactly equal to p or q.
            # This is the Lowest Common Ancestor. Return it immediately.
            else:
                return curr