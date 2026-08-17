class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid  # Target found 🎯
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right sub-array ➡️
            else:
                right = mid - 1  # Target is in the left sub-array 👈
                
        # Target was not found; 'left' holds the correct insert index 📍
        return left