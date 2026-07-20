class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Calculates the number of distinct ways to climb n steps 
        when taking 1 or 2 steps at a time.
        
        Parameters:
        - n (int): The target step number.
        
        Returns:
        - int: The total count of distinct paths to reach step n.
        """
        # Base case: to reach 0 steps or 1 step, there is 1 way
        prev1, prev2 = 1, 1
        
        # Iteratively build up the count for each step up to n
        for _ in range(n - 1):
            temp = prev1
            prev1 = prev1 + prev2
            prev2 = temp
            
        return prev1