class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.li = []
        candidates.sort()

        self.recurse(candidates, target, 0, 0, [])

        return self.li



    def recurse(self, candidates: List[int], target: int, idx: int, currSum: int, currList: List[int]) -> None:
        # base case
        if currSum == target:
            self.li.append(currList.copy())
            return

        if currSum > target: return

        # logic
        for i in range(idx, len(candidates)):

            # if prev same is not considered, do not consider this as well
            if i > idx and candidates[i] == candidates[i-1]: continue

            currSum += candidates[i]
            currList.append(candidates[i])

            self.recurse(candidates, target, i + 1, currSum, currList)

            currSum -= candidates[i]
            currList.pop()



        