"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}  # Maps original node -> cloned node 🗺️

        def dfs(curr):
            if not curr:
                return None
            
            # Base case: Return existing clone if already created 🔄
            if curr in old_to_new:
                return old_to_new[curr]
            
            # Create new node copy 🆕
            copy = Node(curr.val)
            old_to_new[curr] = copy
            
            # Recursively copy all neighbors 👥
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))
                
            return copy

        return dfs(node)
        