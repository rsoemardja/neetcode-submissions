class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 1. Sort intervals by start time 🔢
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # 2. If list is empty or current interval doesn't overlap 🟢
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 3. Overlap detected: extend the current merged interval 🔄
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged