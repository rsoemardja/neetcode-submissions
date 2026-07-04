# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # MAIN SWEEP: Walk through the main facility
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # 1. If the main tree is empty, subRoot cannot be a subtree
        if not root:
            return False
            
        # 2. Check if the tree rooted at the current node matches the blueprint
        if self.isSameTree(root, subRoot):
            return True
            
        # 3. Otherwise, search down the left wing or the right wing
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    # EXACT MATCH TEST: Check if two trees are identical clone configurations
    def isSameTree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        # 1. Both are empty -> match
        if not t1 and not t2:
            return True
        # 2. One is empty or values don't match -> mismatch
        if not t1 or not t2 or t1.val != t2.val:
            return False
            
        # 3. Structural check: Left sides must match AND right sides must match
        return self.isSameTree(t1.left, t2.left) and self.isSameTree(t1.right, t2.right)
        