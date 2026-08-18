class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        # Step 1: Sort candidates to handle duplicates and allow early pruning
        candidates.sort()
        res = []
        
        def backtrack(start: int, target: int, path: list[int]):
            # Base Case: Found a valid combination
            if target == 0:
                res.append(list(path))
                return
            
            # Explore candidates from 'start' to the end of the array
            for i in range(start, len(candidates)):
                # Pruning: Numbers are sorted, so if candidates[i] > target, all remaining are also too large
                if candidates[i] > target:
                    break
                
                # Duplicate Avoidance: Skip identical elements at the same decision depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Choose: Add candidate to path
                path.append(candidates[i])
                
                # Explore: Move to 'i + 1' because each number can only be used ONCE
                backtrack(i + 1, target - candidates[i], path)
                
                # Un-choose: Remove candidate from path to try the next option
                path.pop()
                
        # Start recursion from index 0 with initial target and empty path
        backtrack(0, target, [])
        return res