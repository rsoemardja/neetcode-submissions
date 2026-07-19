class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the contiguous subarray within nums which has the largest sum.
        
        Parameters:
        - nums (list[int]): An array of integers.
        
        Returns:
        - int: The maximum sum found.
        """
        # Initialize both the global maximum and the current subarray running sum
        # with the first element of the array.
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Iterate through the array starting from the second element
        for num in nums[1:]:
            # Core Decision: Is it better to extend the existing subarray 
            # or start a new subarray right at the current number?
            current_sum = max(num, current_sum + num)
            
            # Update the global maximum if the current subarray sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
                
        return max_sum