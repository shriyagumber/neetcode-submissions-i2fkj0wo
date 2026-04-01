class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        li = self.map[key]
        return self.binarySearch(li, timestamp)
    
    def binarySearch(self, li: List[List[int]], timestamp: int) -> str:
        lo = 0
        hi = len(li) - 1

        ans = ""
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if li[mid][0] <= timestamp:
                ans = li[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
                
        
        return ans

        
