class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        map = {}

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in map: return False
            
            map[t[i]] -= 1
            if map[t[i]] < 0: return False
        
        return True

        