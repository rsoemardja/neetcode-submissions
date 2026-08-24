class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        # Step 1: Map each character to its alien alphabet rank 🗂️
        order_map = {char: i for i, char in enumerate(order)}
        
        # Step 2: Compare adjacent word pairs 👥
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            
            for j in range(len(w1)):
                # Prefix case: w1 is longer than w2 (e.g., "neetcode" vs "neet")
                if j == len(w2):
                    return False
                
                # Different characters found: check their relative rank
                if w1[j] != w2[j]:
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    # Correct order confirmed for this pair, move to next pair
                    break
                    
        return True