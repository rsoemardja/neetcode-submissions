import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # 1. INVENTORY SETUP: Invert the signs to create a Max-Heap using Python's Min-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # 2. SIMULATION LOOP: Continue as long as there are at least two items to smash
        while len(max_heap) > 1:
            # Retrieve the two heaviest elements (and make them positive values again)
            first = -heapq.heappop(max_heap)
            second = -heapq.heappop(max_heap)
            
            # If they aren't equal, the remainder goes back into the heap
            if first != second:
                leftover = first - second
                heapq.heappush(max_heap, -leftover)
                
        # 3. REPORT STATUS
        # If one element remains, invert it back to positive. If none remain, return 0.
        return -max_heap[0] if max_heap else 0