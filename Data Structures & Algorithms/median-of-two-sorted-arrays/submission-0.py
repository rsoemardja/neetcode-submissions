class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # System Requirement: Ensure A is the smaller array to guarantee O(log(min(m, n)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            # i is the partition index for array A
            i = (l + r) // 2  
            # j is the balancing partition index for array B
            j = half - (i + 1) - 1 
            
            # Boundary protections: Handle cases where the divider falls at the very edges
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Check if partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # ODD TOTAL LENGTH: The median is simply the smallest element on the right side
                if total % 2 != 0:
                    return min(Aright, Bright)
                # EVEN TOTAL LENGTH: Average of the maximum left boundary and minimum right boundary
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0
                
            elif Aleft > Bright:
                # Too many elements from A are on the left side, shift our binary search pointer left
                r = i - 1
            else:
                # Too few elements from A are on the left side, shift our binary search pointer right
                l = i + 1