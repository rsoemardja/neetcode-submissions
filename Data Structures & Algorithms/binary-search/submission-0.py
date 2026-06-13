class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle of our current zone
            mid = (left + right) // 2
            
            # 1. Did we find it?
            if nums[mid] == target:
                return mid
            
            # 2. If the middle is too small, look at the right half
            elif nums[mid] < target:
                left = mid + 1
                
            # 3. If the middle is too big, look at the left half
            else:
                right = mid - 1
        
        # If we finish the loop and haven't found it, it's not here
        return -1