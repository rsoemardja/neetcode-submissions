class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        """
        Simulates collisions between asteroids moving in 1D space.
        
        Parameters:
            asteroids (list[int]): Sizes and directions of asteroids.
            
        Returns:
            list[int]: The state of asteroids after all collisions.
        """
        stack = []
        
        for a in asteroids:
            # A collision happens if stack top is moving right (>0) 
            # and current asteroid 'a' is moving left (<0)
            while stack and stack[-1] > 0 and a < 0:
                diff = stack[-1] + a  # Compare sizes (since a is negative)
                
                if diff < 0:
                    # Top of stack is smaller and explodes
                    stack.pop()
                elif diff == 0:
                    # Both are equal size, both explode
                    stack.pop()
                    break
                else:
                    # Incoming asteroid 'a' is smaller and explodes
                    break
            else:
                # Executes if the while loop did NOT break 
                # (meaning 'a' survived all collisions)
                stack.append(a)
                
        return stack