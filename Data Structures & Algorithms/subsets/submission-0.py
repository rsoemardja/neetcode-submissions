class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all possible subsets (the power set) of a unique integer array.
        
        Parameters:
        - nums (list[int]): An array of unique integers.
        
        Returns:
        - list[list[int]]: A list containing all generated subsets.
        """
        result = []
        current_subset = []
        
        def backtrack(i: int):
            # Base Case: If the index matches the length of the array,
            # we have made a choice for every element. Save this subset.
            if i == len(nums):
                result.append(current_subset.copy())
                return
            
            # Decision 1: INCLUDE the current element nums[i]
            current_subset.append(nums[i])
            backtrack(i + 1)
            
            # Decision 2: EXCLUDE the current element nums[i]
            # We pop the element out to clean up the state before branching right
            current_subset.pop()
            backtrack(i + 1)
            
        # Start the recursive search from the 0-th index
        backtrack(0)
        return result