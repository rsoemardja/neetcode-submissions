class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid is greater than right, we are in the "left mountain"
            # and the cliff is to the right.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If mid is less than or equal to right, we are in the 
            # "right mountain" and the minimum is at mid or to the left.
            else:
                right = mid
                
        # When left == right, we've converged on the minimum!
        return nums[left]