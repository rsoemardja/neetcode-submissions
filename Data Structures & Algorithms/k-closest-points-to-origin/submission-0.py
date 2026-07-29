import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        max_heap = []  # Max-heap storing (-distance, [x, y]) 🎯
        
        for x, y in points:
            dist = x * x + y * y  # Squared Euclidean distance 📏
            
            # Python's heapq is a Min-Heap, so we negate distance to simulate a Max-Heap 💡
            heapq.heappush(max_heap, (-dist, [x, y]))
            
            # Keep only the k closest elements 🗑️
            if len(max_heap) > k:
                heapq.heappop(max_heap)
                
        # Extract and return the coordinates 📍
        return [point for neg_dist, point in max_heap]