# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # Base case: if left and right are the same, no reversal is needed
        if left == right or not head:
            return head
        
        # Step 1: Create a dummy node to handle edge cases easily (e.g., left = 1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 2: Move 'prev' to the node right BEFORE the sublist starts
        for _ in range(left - 1):
            prev = prev.next
            
        # 'curr' is the first node of the sublist that will be reversed
        curr = prev.next
        
        # Step 3: Reverse the sublist in-place using a 3-pointer swap
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
            
        return dummy.next
        