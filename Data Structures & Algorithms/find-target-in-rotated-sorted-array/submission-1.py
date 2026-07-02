class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 1. POSITIONS: Setup our boundary guards
        left = 0
        right = len(nums) - 1
        
        # 2. PATROL LOOP: Binary search
        while left <= right:
            mid = (left + right) // 2
            
            # Found the target!
            if nums[mid] == target:
                return mid
            
            # Check if the LEFT side is an unbroken sorted ramp
            if nums[left] <= nums[mid]:
                # Is the target cleanly inside this unbroken left segment?
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left half
                else:
                    left = mid + 1   # Search right half
                    
            # Otherwise, the RIGHT side must be the unbroken sorted ramp
            else:
                # Is the target cleanly inside this unbroken right segment?
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right half
                else:
                    right = mid - 1  # Search left half
                    
        # 3. ALARM: Element not found
        return -1