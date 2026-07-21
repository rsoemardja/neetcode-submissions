# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # Dummy head node to easily build the result list 🏷️
        current = dummy
        carry = 0
        
        # Loop continues while there are nodes left to process or a carry remains 🔄
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and updated carry ➕
            total = val1 + val2 + carry
            carry = total // 10    # Value to carry over (0 or 1)
            digit = total % 10     # Single digit stored in the node
            
            # Attach new node to the result list 🔗
            current.next = ListNode(digit)
            current = current.next
            
            # Advance pointers in the input lists ➡️
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next  # Return head of the generated list