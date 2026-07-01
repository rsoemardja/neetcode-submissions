# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. STAGING: Create a dummy node to gracefully handle removing the first node
        dummy = ListNode(0)
        dummy.next = head
        
        fast = head
        slow = dummy
        
        # 2. HEAD START: Advance Guard 1 (fast) 'n' steps ahead
        for _ in range(n):
            fast = fast.next
            
        # 3. SYNCED PATROL: Move both guards until Guard 1 steps off the edge
        while fast:
            fast = fast.next
            slow = slow.next
            
        # 4. THE BYPASS: Guard 2 (slow) is right before the target. Skip the target!
        slow.next = slow.next.next
        
        # 5. REPORT: Return the actual head of the modified list
        return dummy.next