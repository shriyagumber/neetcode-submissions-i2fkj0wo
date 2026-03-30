class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1])
        count = 0

        lastEnd = intervals[0][1]
        for i in range(1, n):
            if intervals[i][0] < lastEnd:
                count += 1
            else:
                lastEnd = intervals[i][1]
        
        return count


