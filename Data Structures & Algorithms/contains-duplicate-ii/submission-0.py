class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        """
        Checks if there are two duplicate values within 'k' distance of each other.
        """
        # Stores the most recent index seen for each number 🗺️
        seen = {}
        
        for i, num in enumerate(nums):
            # If we've seen this number before, check the index difference 📏
            if num in seen and i - seen[num] <= k:
                return True
            
            # Update the number's most recent index 📌
            seen[num] = i
            
        return False