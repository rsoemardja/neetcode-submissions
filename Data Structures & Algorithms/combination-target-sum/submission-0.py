class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        Finds all unique combinations in nums that sum up to target.
        Numbers can be reused an unlimited number of times.
        """
        res = []

        def backtrack(i: int, current_comb: list[int], current_sum: int):
            # Base Case 1: Success! We reached the target sum 🎯
            if current_sum == target:
                res.append(current_comb.copy())
                return
            
            # Base Case 2: Out of bounds or sum exceeded 🛑
            if i >= len(nums) or current_sum > target:
                return

            # Choice 1: Include nums[i] in the current combination ➕
            # (We keep 'i' the same because we can reuse the same element!)
            current_comb.append(nums[i])
            backtrack(i, current_comb, current_sum + nums[i])
            
            # Backtrack step: undo the choice ↩️
            current_comb.pop()

            # Choice 2: Skip nums[i] and move to the next index ➡️
            backtrack(i + 1, current_comb, current_sum)

        backtrack(0, [], 0)
        return res