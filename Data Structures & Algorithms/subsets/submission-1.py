class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.re = []
        self.dfs(nums, [], 0)
        return self.re


    def dfs(self, nums: List[int], currList: List[int], idx: int) -> None:
        # add to the final list
        if idx == len(nums): 
            self.re.append(currList.copy())
            return

        # add to the currList
        currList.append(nums[idx])
        self.dfs(nums, currList, idx+1)

        # do not add to the currList
        currList.pop()
        self.dfs(nums, currList, idx+1)