class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.li = []
        self.dfs(nums, 0, [])
        return self.li
    
    def dfs(self, nums: List[int], idx: int, currList: List[int]) -> None:
        # base case
        self.li.append(currList.copy())

        # logic
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]: continue

            currList.append(nums[i])
            self.dfs(nums, i + 1, currList)
            currList.pop()





        