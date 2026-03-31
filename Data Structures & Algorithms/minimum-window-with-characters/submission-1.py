class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # gathering the frequency of t
        freqT = {}
        for i in range(len(t)):
            ch = t[i]
            if ch not in freqT: freqT[ch] = 0
            freqT[ch] += 1
        

        lo = 0
        smallLen = len(s)
        loIdx = -1
        hiIdx = -1
        count = 0

        for i in range(len(s)):
            ch = s[i]

            if ch in freqT:
                freqT[ch] -= 1
                if freqT[ch] == 0: 
                    count += 1
        
            # can we have it smaller, if we have achieved the required
            while count == len(freqT):

                if smallLen >= i - lo + 1:
                    smallLen = i - lo + 1
                    loIdx = lo
                    hiIdx = i

                chLo = s[lo]

                if chLo in freqT:
                    freqT[chLo] += 1
                    if freqT[chLo] == 1:
                        count -= 1
                
                lo += 1
                

        if loIdx == -1: return ""
        return s[loIdx:hiIdx+1]
                
                



        