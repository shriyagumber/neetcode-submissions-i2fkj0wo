class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = 0
        for num in nums: tot+=num
        if tot % 2 == 1: return False
        target = tot/2
        return self.recurse(nums, 0, target)

    def recurse(self, nums: List[int], idx: int, target: int) -> bool:
        if target == 0: return True
        if target < 0: return False
        if idx == len(nums): return False

        # include
        if self.recurse(nums, idx+1, target - nums[idx]) or self.recurse(nums, idx+1, target):
            return True
        else:
            return False

       





        