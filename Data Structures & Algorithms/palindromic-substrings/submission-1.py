class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        for i in range(n):

            lo = i
            hi = i
            # odd
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1

            lo = i-1
            hi = i
            # even
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                count += 1
                lo -= 1
                hi += 1
        

        return count

        
        