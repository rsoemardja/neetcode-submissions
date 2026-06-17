class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, no cycle is possible
        if not head or not head.next:
            return False
        
        # State: Both pointers start at the head
        slow = head
        fast = head
        
        # Loop: Move as long as the 'fast' pointer can keep moving
        while fast and fast.next:
            slow = slow.next          # Slow moves 1 step
            fast = fast.next.next     # Fast moves 2 steps
            
            # Action: If the fast pointer laps the slow one, they meet
            if slow == fast:
                return True
                
        # If the loop finishes, 'fast' hit the end of the list
        return False