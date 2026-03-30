class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        setCh = set()
        lo = 0
        maxLen = 0

        for i in range(n):
            ch = s[i]

            while ch in setCh:
                setCh.remove(s[lo])
                lo += 1
            
            setCh.add(ch)

            maxLen = max(maxLen, i - lo + 1)

        return maxLen

