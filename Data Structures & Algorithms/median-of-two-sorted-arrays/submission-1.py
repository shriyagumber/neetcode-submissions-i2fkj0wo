class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if m > n: return self.findMedianSortedArrays(nums2, nums1)

        lo = 0
        hi = m

        while lo <= hi:
            mid = lo + (hi - lo)//2

            if mid > 0: L1 = nums1[mid-1]
            else: L1 = float('-inf')

            if mid < m: R1 = nums1[mid]
            else: R1 = float('inf')

            mid2 = (m + n) // 2 - mid

            if mid2 > 0: L2 = nums2[mid2-1]
            else: L2 = float('-inf')

            if mid2 < n: R2 = nums2[mid2]
            else: R2 = float('inf')

            if L1 <= R2 and L2 <= R1:
                if (n + m) % 2 == 0: return (float)(max(L1,L2) + min(R1,R2))/2.0
                else: return min(R1, R2)
            elif L1 >= R2:
                hi = mid - 1
            else:
                lo = mid + 1
                
    
        return -1