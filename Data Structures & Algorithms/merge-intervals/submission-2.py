class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n = len(intervals)

        re = []
        re.append(intervals[0])

        for i in range(1,n):
            if re[-1][1] >= intervals[i][0]:
                re[-1][1] = max(re[-1][1], intervals[i][1])
            else:
                re.append(intervals[i])
        
        return re
        
        