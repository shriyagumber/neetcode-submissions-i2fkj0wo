class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        lo = 0
        maxLen = 0
        
        map = {}

        for i in range(n):
            map[s[i]] = 1 + map.get(s[i], 0)

            while (i - lo + 1) - max(map.values()) > k:
                map[s[lo]] -= 1
                lo += 1
            
            maxLen = max(maxLen, i-lo+1)
        
        return maxLen


        