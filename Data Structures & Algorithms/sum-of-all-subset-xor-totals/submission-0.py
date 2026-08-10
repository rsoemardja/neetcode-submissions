class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        """
        Calculates the sum of XOR totals for all subsets using DFS.
        """
        def dfs(index: int, current_xor: int) -> int:
            # Base case: we've made decisions for all elements 🎯
            if index == len(nums):
                return current_xor
            
            # Choice 1: Include nums[index] in the subset ➕
            include = dfs(index + 1, current_xor ^ nums[index])
            
            # Choice 2: Exclude nums[index] from the subset ➖
            exclude = dfs(index + 1, current_xor)
            
            # Total sum from both branches 🔀
            return include + exclude
            
        return dfs(0, 0)