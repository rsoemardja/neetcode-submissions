class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Calculates the number of ways to decode a numeric string into letters ('A'-'Z').
        
        Parameters:
            s (str): A string containing digit characters.
            
        Returns:
            int: The total number of valid decoding combinations.
        """
        # Edge case: If the string is empty or starts with '0', it cannot be decoded.
        if not s or s[0] == '0':
            return 0
            
        n = len(s)
        
        # dp1 represents dp[i + 1] (initialized for base case at position n)
        # dp2 represents dp[i + 2] (initialized for base case at position n + 1)
        dp1 = 1  
        dp2 = 0  
        
        # Traverse the string backwards from the last character to the first
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                current = 0  # Leading zero cannot form a valid character
            else:
                # Choice 1: Take 1 digit (contributes dp[i + 1] ways)
                current = dp1
                
                # Choice 2: Take 2 digits if s[i:i+2] is between "10" and "26"
                if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
                    current += dp2
            
            # Shift variables for the next iteration (moving leftwards)
            dp2 = dp1
            dp1 = current
            
        return dp1