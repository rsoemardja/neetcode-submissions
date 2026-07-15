class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        """
        Counts and returns the number of islands in a 2D grid.
        
        Parameters:
        - grid (list[list[str]]): A 2D grid of '1's (land) and '0's (water).
        
        Returns:
        - int: The total count of distinct islands.
        """
        if not grid or not grid[0]:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0
        
        def dfs(r: int, c: int):
            # Base Case: Stop if out of bounds or if the cell is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
                
            # Mark the current cell as visited by converting it to water
            grid[r][c] = '0'
            
            # Recursively explore all four neighboring directions
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Iterate through every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # A new island is discovered
                    island_count += 1
                    # Perform DFS to submerge/mark the entire island
                    dfs(r, c)
                    
        return island_count