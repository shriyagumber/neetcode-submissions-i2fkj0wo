class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        best = [-1, -1, -1]

        for triplet in triplets:
            first, second, third = triplet

            if first > target[0] or second > target[1] or third > target[2]: continue
            best = [max(first, best[0]), max(second, best[1]), max(third, best[2])]
        

        return best == target