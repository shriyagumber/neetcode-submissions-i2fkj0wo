class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        self.re = []
        self.dfs(nums, seen, [])
        return self.re

    def dfs(self, nums: List[int], seen: set[int], currList: List[int]) -> None:
        # base case
        if len(currList) == len(nums):
            self.re.append(currList.copy())
            return

        # logic
        for i in range(len(nums)):
            if nums[i] not in seen:
                currList.append(nums[i])
                seen.add(nums[i])
                self.dfs(nums, seen, currList)
                currList.pop()
                seen.remove(nums[i])