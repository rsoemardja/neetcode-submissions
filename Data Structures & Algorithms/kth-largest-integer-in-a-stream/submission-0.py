

class KthLargest:
    # 1. SETUP: Create a VIP room (min-heap) with a strict capacity limit 'k'.
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        # Turn the list into a functioning min-heap structure
        heapq.heapify(self.min_heap)
        
        # 2. INITIALIZE: Kick out the shortest ones if we exceed 'k'
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    # 3. WHEN A NEW PERSON ARRIVES
    def add(self, val: int) -> int:
        # Push the new person into the room
        heapq.heappush(self.min_heap, val)
        
        # If the room is now over capacity (> k), kick out the shortest person
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # Return the height of the shortest person currently left in the room
        return self.min_heap[0]
        
