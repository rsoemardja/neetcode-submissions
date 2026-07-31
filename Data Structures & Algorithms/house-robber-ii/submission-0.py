class Solution:
    def rob(self, nums: list[int]) -> int:
        # Edge case: If there is only 1 house, rob it! 🏠
        if len(nums) == 1:
            return nums[0]

        # Helper function to solve standard linear House Robber (O(1) space) 💰
        def rob_linear(houses: list[int]) -> int:
            rob1, rob2 = 0, 0
            for n in houses:
                # Decide: rob current house + rob1, OR skip current house (keep rob2)
                new_rob = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2

        # House 0 and House n-1 are neighbors, so we cannot rob both! 🚫
        # Choice 1: Consider houses from index 0 to n-2 (exclude last house)
        # Choice 2: Consider houses from index 1 to n-1 (exclude first house)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))