class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        Generates all possible permutations of a list of unique integers.
        
        Parameters:
            nums (list[int]): A list of unique integers.
            
        Returns:
            list[list[int]]: A list containing all possible permutations.
        """
        results = []
        visited = [False] * len(nums)

        def backtrack(current_permutation: list[int]):
            # Base Case: If the current permutation is the same length as nums,
            # we have formed a valid complete permutation.
            if len(current_permutation) == len(nums):
                # Save a copy of the current permutation to our results list
                results.append(list(current_permutation))
                return

            # Recursive Case: Try adding each unused number to the current permutation
            for i in range(len(nums)):
                if not visited[i]:
                    # Choose: Mark the element as used and append it
                    visited[i] = True
                    current_permutation.append(nums[i])

                    # Explore: Recurse to fill the next position
                    backtrack(current_permutation)

                    # Backtrack: Undo the choice so other branches can use this element
                    current_permutation.pop()
                    visited[i] = False

        # Start the recursive backtracking with an empty permutation
        backtrack([])
        return results


# --- Example Usage ---
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    test_nums = [1, 2, 3]
    output = solution.permute(test_nums)
    print("Input:", test_nums)
    print("Permutations:", output)