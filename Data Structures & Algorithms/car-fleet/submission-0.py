class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Create pairs of (position, speed) and sort by position descending
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        stack = []
        for pos, spd in cars:
            # Time for this car to reach the target
            time = (target - pos) / spd
            
            # If stack is empty or this car takes longer than the car 
            # in front, it forms a new fleet
            if not stack or time > stack[-1]:
                stack.append(time)
            # Else: it catches up and becomes part of the existing fleet
            
        return len(stack)
 