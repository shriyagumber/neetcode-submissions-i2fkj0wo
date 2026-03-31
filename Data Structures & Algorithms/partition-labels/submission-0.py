class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        pos = [-1] * 26

        for i in range(len(s)):
            ch = s[i]
            pos[ord(ch) - ord('a')] = i
        
        
        re = []
        i = 0

        while i < len(s):

            currMax = pos[ord(s[i]) - ord('a')]
            j = i

            while j < currMax:
                lastPos = pos[ord(s[j]) - ord('a')]
                currMax = max(currMax, lastPos)
                j += 1
            

            re.append(currMax - i + 1)

            i = currMax + 1
        
        return re

            
            


        