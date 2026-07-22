class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # Phase 1: Find the intersection point inside the cycle 🔄
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]          # Moves 1 step 🐢
            fast = nums[nums[fast]]    # Moves 2 steps 🐇
            if slow == fast:
                break
                
        # Phase 2: Find the entrance to the cycle (the duplicate number) 🎯
        slow = nums[0]                 # Reset slow to the start
        
        while slow != fast:
            slow = nums[slow]          # Moves 1 step 🐢
            fast = nums[fast]          # Moves 1 step 🐢 (now matching slow's speed)
            
        return slow  # The meeting point is the duplicate value!