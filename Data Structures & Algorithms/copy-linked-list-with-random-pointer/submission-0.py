from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Creates a deep copy of a linked list where each node has a random pointer.
        
        Parameters:
        - head (Node): The head node of the original linked list.
        
        Returns:
        - Node: The head node of the newly copied linked list.
        """
        if not head:
            return None
            
        # This hash map associates original nodes to their cloned copies.
        # We pre-populate it with {None: None} to gracefully handle 
        # null next or random pointers during the connection phase.
        old_to_new = {None: None}
        
        # --- Pass 1: Create a copy of all nodes and store them in the map ---
        current = head
        while current:
            cloned_node = Node(current.val)
            old_to_new[current] = cloned_node
            current = current.next
            
        # --- Pass 2: Connect the next and random pointers for each copy ---
        current = head
        while current:
            cloned_node = old_to_new[current]
            
            # Use the hash map to find the correct cloned nodes to point to
            cloned_node.next = old_to_new[current.next]
            cloned_node.random = old_to_new[current.random]
            
            current = current.next
            
        # Return the copy of the head node
        return old_to_new[head]