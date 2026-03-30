class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_s = "".join(ch.lower() for ch in s if ch.isalnum())
        
        l = 0
        r = len(alpha_s) - 1

        while (l < r):
            if alpha_s[l] != alpha_s[r]: return False
            l += 1
            r -= 1
        
        return True
            



        