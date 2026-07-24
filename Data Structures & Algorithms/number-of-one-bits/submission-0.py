class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        
        while n > 0:
            count += n & 1  # 1. Add 1 if the lowest bit is set 🔢
            n >>= 1         # 2. Shift bits right by 1 position ➡️
            
        return count