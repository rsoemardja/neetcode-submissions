class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1 as a substring.
        
        Parameters:
        - s1 (str): The string whose permutations we are looking for.
        - s2 (str): The target string to search within.
        
        Returns:
        - bool: True if a permutation of s1 is a substring of s2, False otherwise.
        """
        len1, len2 = len(s1), len(s2)
        
        # Edge Case: If s1 is longer than s2, s2 cannot possibly contain its permutation.
        if len1 > len2:
            return False
            
        # Initialize fixed-size arrays of size 26 to track lowercase letter frequencies
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Step 1: Populate the frequency map for s1 and the very first window of s2
        for i in range(len1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        # If the first window matches, we are done
        if s1_count == s2_count:
            return True
            
        # Step 2: Slide the window across the remaining characters of s2
        for i in range(len1, len2):
            # Add the new character entering the right side of the window
            right_char_idx = ord(s2[i]) - ord('a')
            s2_count[right_char_idx] += 1
            
            # Remove the old character exiting the left side of the window
            left_char_idx = ord(s2[i - len1]) - ord('a')
            s2_count[left_char_idx] -= 1
            
            # Check if the updated window matches s1's character profile
            if s1_count == s2_count:
                return True
                
        return False