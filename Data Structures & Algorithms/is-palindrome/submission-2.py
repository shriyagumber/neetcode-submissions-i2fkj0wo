class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        s = s.lower()
        lo = 0
        hi = n - 1

        while lo < hi:
            while (lo < hi and not s[lo].isalnum()):
                lo += 1

            while (hi > lo and not s[hi].isalnum()):
                hi -= 1
            
            if lo < hi and s[lo] != s[hi]: return False
            else:
                lo += 1
                hi -= 1
        
        return True
            



        