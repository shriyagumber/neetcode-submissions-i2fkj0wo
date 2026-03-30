class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.re = []
        self.dfs(nums, target, 0, [], 0)
        return self.re
    
    def dfs(self, nums: List[int], target: int, idx: int, currList: List[int], currSum: int) -> None:
        if currSum == target:
            self.re.append(currList.copy())
            return
        
        if idx == len(nums) or currSum > target:
            return
        
        for i in range(idx, len(nums)):
            # add the current number
            currList.append(nums[i])
            currSum += nums[i]

            # dfs
            self.dfs(nums, target, i, currList, currSum)

            # without the current number
            currList.remove(nums[i])
            currSum -= nums[i]

        
        