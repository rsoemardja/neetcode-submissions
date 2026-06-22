class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 1. State: 
        # result array initialized to 0 (default if no warmer day is found)
        # stack stores the indices of days we are still waiting for a warmer temp
        n = len(temperatures)
        result = [0] * n
        stack = [] 
        
        # 2. Loop: 
        # Iterate through every day in the sequence
        for i in range(n):
            current_temp = temperatures[i]
            
            # 3. Action: 
            # While we have a stack and the current day is warmer 
            # than the temperature at the index on top of the stack...
            while stack and current_temp > temperatures[stack[-1]]:
                # We found a warmer day for the index at the top of the stack!
                prev_index = stack.pop()
                
                # The distance is the difference in indices
                result[prev_index] = i - prev_index
            
            # Push the current index onto the stack to wait for its warmer day
            stack.append(i)
            
        return result