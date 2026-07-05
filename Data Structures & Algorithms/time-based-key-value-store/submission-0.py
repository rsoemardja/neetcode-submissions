class TimeMap:
    # 1. DATA STRUCTURE SETUP
    def __init__(self):
        # Maps string -> list of [timestamp, value]
        self.store = {}

    # 2. SET PROTOCOL
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    # 3. GET PROTOCOL
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # If the key was never recorded, return empty string
        if key not in self.store:
            return res
            
        pairs = self.store[key]
        left, right = 0, len(pairs) - 1
        
        # Binary Search loop
        while left <= right:
            mid = (left + right) // 2
            
            # If the logged timestamp is in the past or exactly matches target
            if pairs[mid][0] <= timestamp:
                res = pairs[mid][1]   # Save this as our best candidate so far
                left = mid + 1        # Look right to find a closer/more recent timestamp
            else:
                right = mid - 1       # Too far in the future, look left
                
        return res
        
