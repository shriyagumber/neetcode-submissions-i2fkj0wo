"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        numRooms = 0

        # using heaps
        occupied = []
        available = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # freeing up all occupied till/before the start
            while len(occupied) > 0 and occupied[0][0] <= start:
                _, roomID = heapq.heappop(occupied)
                available.append(roomID)

            if len(available) == 0:
                available.append(numRooms)
                numRooms += 1
            
            topRoom = available.pop()
            heapq.heappush(occupied, [end, topRoom])
        
        return numRooms


        

        