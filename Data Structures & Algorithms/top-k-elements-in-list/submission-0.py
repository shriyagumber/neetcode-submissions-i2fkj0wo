class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        map = {}
        pq = []

        for i in range(n):
            if nums[i] in map:
                map[nums[i]] += 1
            else:
                map[nums[i]] = 1
        

        for key in map.keys():
            heapq.heappush(pq, (-map[key], key))
        
        re = []
        for i in range(k):
            _, val = heapq.heappop(pq)
            re.append(val)

        return re        