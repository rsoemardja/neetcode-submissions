from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level order traversal of a binary tree.
        
        Parameters:
        - root (TreeNode): The root node of the binary tree.
        
        Returns:
        - List[List[int]]: A nested list representing the node values level by level.
        """
        # Return an empty list if the tree contains no nodes
        if not root:
            return []
            
        result = []
        
        # Initialize a double-ended queue with the root node
        queue = deque([root])
        
        while queue:
            # The number of nodes at the current level is the queue's current size
            level_size = len(queue)
            current_level = []
            
            # Process all nodes belonging to the current level
            for _ in range(level_size):
                # Pop from the left (front) of the queue in O(1) time
                node = queue.popleft()
                current_level.append(node.val)
                
                # If a left child exists, queue it for the next level
                if node.left:
                    queue.append(node.left)
                # If a right child exists, queue it for the next level
                if node.right:
                    queue.append(node.right)
            
            # Append the fully populated level list to our master result
            result.append(current_level)
            
        return result