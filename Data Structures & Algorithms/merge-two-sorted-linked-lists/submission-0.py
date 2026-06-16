# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. State: Create a dummy node to act as the "anchor"
        dummy = ListNode()
        tail = dummy # 'tail' will always point to the end of our new list
        
        # 2. Loop: Move as long as both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next # Move our anchor forward
            
        # 3. Cleanup: If one list runs out, attach the remainder of the other
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next