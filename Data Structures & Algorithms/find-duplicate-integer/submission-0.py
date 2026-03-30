class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        start = nums[0]

        while True:
            temp = nums[start]
            if nums[start] == 0: return start
            nums[start] = 0
            start = temp

        return 1

        