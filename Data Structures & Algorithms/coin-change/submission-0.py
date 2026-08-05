class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Finds the minimum number of coins needed to make up a target amount.
        
        Parameters:
            coins (list[int]): Available coin denominations.
            amount (int): Target monetary amount.
            
        Returns:
            int: Fewest number of coins required, or -1 if impossible.
        """
        # Initialize DP array with 'infinity' representing unachievable states.
        # dp[i] stores the minimum coins needed to make amount 'i'.
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins are needed to make an amount of 0 🎯
        dp[0] = 0
        
        # Compute minimum coins for every amount from 1 up to 'amount' 📈
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # Choose minimum between current value and (1 coin + remaining amount) 💡
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        # Return result: if dp[amount] is still infinity, it's impossible (-1) 🚫
        return dp[amount] if dp[amount] != float('inf') else -1