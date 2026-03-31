class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currMinProd = nums[0]
        currMaxProd = nums[0]
        maxProd = nums[0]

        for i in range(1,n):
            valMin = currMinProd
            valMax = currMaxProd

            currMinProd = min(valMin * nums[i], valMax * nums[i], nums[i])
            currMaxProd = max(valMin * nums[i], valMax * nums[i], nums[i])
            maxProd = max(maxProd, currMaxProd)

        return maxProd