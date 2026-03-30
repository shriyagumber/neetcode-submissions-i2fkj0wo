class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        n = len(stones)

        for i in range(n): heapq.heappush(pq, -stones[i])

        while len(pq) > 1:
            first = - heapq.heappop(pq)
            second = - heapq.heappop(pq)

            if first > second:
                newVal = first - second
                heapq.heappush(pq, -newVal)
        

        if len(pq) == 0: return 0
        else: return -pq[0]

        


        