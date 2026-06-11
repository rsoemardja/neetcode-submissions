public class Solution {
    public int CharacterReplacement(string s, int k) {
        // 1. THE SCOREBOARD: 26 slots to count frequencies of letters 'A' through 'Z'
        int[] letterCounts = new int[26];
        
        // 2. CAMERA POINTERS & STATE TELEMETRY
        int left = 0;
        int maxWindowSeen = 0;
        int championCount = 0; // Tracks the highest count of a single letter inside the current window

        // 3. THE EXPANSION ENGINE: Move the right edge of the window forward frame-by-frame
        for (int right = 0; right < s.Length; right++) {
            // Find the character's array address index (0 to 25)
            int currentCharIdx = s[right] - 'A';
            
            // Increment its count on our scoreboard
            letterCounts[currentCharIdx]++;
            
            // Update our champion record if this letter now dominates the window view
            if (letterCounts[currentCharIdx] > championCount) {
                championCount = letterCounts[currentCharIdx];
            }

            // 4. THE BUDGET CHECK
            int currentWindowLength = right - left + 1;
            int potholesToFix = currentWindowLength - championCount;

            // If we are over budget (more potholes than our asphalt budget k can fix)
            if (potholesToFix > k) {
                // Dump the leftmost character out of our scoreboard before we shift
                int leftCharIdx = s[left] - 'A';
                letterCounts[leftCharIdx]--;
                
                // Slide the left pointer inward to shrink the window back down
                left++;
            }

            // 5. RECORD TELEMETRY: Measure our maximum validated window size
            int validatedWindowLength = right - left + 1;
            if (validatedWindowLength > maxWindowSeen) {
                maxWindowSeen = validatedWindowLength;
            }
        }

        // Return the absolute largest smooth stretch we framed
        return maxWindowSeen;
    }
}