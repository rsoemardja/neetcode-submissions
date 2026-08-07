class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Calculates total unique paths from top-left (0,0) to 
        bottom-right (m-1, n-1) in an m x n grid.
        
        Parameters:
            m (int): Number of rows
            n (int): Number of columns
            
        Returns:
            int: Number of unique paths to reach the bottom-right corner.
        """
        # Initialize a row with 1s representing 1 way to reach each cell in row 0 🏁
        dp = [1] * n
        
        # Traverse row by row starting from row 1 ⬇️
        for i in range(1, m):
            for j in range(1, n):
                # Unique paths to (i, j) = paths from above + paths from left ➕
                dp[j] += dp[j - 1]
                
        return dp[-1]