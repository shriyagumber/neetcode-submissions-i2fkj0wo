class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        setNum = set(nums)
        maxLen = 0

    
        for key in setNum:
            if (key - 1) in setNum: continue

            curr = key + 1
            currLen = 1

            while curr in setNum:
                curr += 1
                currLen += 1
            
            maxLen = max(maxLen, currLen)
        
        return maxLen
        