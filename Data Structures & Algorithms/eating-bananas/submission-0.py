import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. State: The search range for k
        left, right = 1, max(piles)
        res = right
        
        # 2. Loop: Binary Search
        while left <= right:
            mid = (left + right) // 2
            
            # Action: Calculate hours needed at speed 'mid'
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p / mid)
            
            # Decision: Is this speed viable?
            if hours_needed <= h:
                res = mid # Potential answer found
                right = mid - 1 # Try to find a smaller k
            else:
                left = mid + 1 # Need to eat faster
                
        return res