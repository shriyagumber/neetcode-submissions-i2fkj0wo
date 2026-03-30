class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        loIdx = -1
        hiIdx = -1
        maxLen = 0

        for i in range(n):

            lo = i
            hi = i
            # odd palindrome
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                if hi - lo + 1 > maxLen:
                    maxLen = hi - lo + 1
                    loIdx = lo
                    hiIdx = hi
                
                lo -= 1
                hi += 1

            lo = i-1
            hi = i
            # even palindrome
            while lo >= 0 and hi < n and s[lo] == s[hi]:
                if hi - lo + 1 > maxLen:
                    maxLen = hi - lo + 1
                    loIdx = lo
                    hiIdx = hi
                
                lo -= 1
                hi += 1
            
        if loIdx == -1: return ""
        else: return s[loIdx : hiIdx+1]





        