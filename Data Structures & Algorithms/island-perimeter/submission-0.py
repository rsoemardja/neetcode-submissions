class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Calculates the total perimeter of an island in a 2D grid.
        
        Parameters:
            grid (list[list[int]]): 2D grid where 1 is land and 0 is water.
            
        Returns:
            int: Total perimeter of the island.
        """
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # Every land cell contributes 4 sides initially 🟩
                    perimeter += 4
                    
                    # If there's a land cell directly above, subtract 2 shared edges ⬆️
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
                        
                    # If there's a land cell directly to the left, subtract 2 shared edges ⬅️
                    if c > 0 and grid[r][c - 1] == 1:
                        perimeter -= 2
                        
        return perimeter