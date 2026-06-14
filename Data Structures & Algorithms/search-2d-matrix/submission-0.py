class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        rows = len(matrix)
        cols = len(matrix[0])
        
        # We treat the matrix as a 1D array of size (rows * cols)
        left = 0
        right = (rows * cols) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Convert 1D index 'mid' back to 2D coordinates
            mid_val = matrix[mid // cols][mid % cols]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False