class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1: return 0

        maxIdx = nums[0]
        currIdx = nums[0]

        count = 1
        for i in range(1, n):
            maxIdx = max(maxIdx, i + nums[i])

            if i != n-1 and i == currIdx:
                count += 1
                currIdx = maxIdx
        
        return count
