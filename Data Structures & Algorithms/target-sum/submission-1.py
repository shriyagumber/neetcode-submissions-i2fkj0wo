class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, target, 0, 0)

    def dfs(self, nums: List[int], target: int, idx: int, currSum: int) -> int:
        if idx == len(nums):
            if currSum == target:
                return 1
            else:
                return 0

        return self.dfs(nums, target, idx+1, currSum + nums[idx]) + self.dfs(nums, target, idx+1, currSum - nums[idx])
        