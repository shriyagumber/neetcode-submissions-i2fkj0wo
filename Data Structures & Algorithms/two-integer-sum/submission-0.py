class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = {}

        for i in range(n):
            find = target - nums[i]

            if find in map:
                return [map[find], i]
            
            map[nums[i]] = i

        return [-1, -1]
        