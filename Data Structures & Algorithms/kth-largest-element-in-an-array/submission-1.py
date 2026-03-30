class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pq = []

        for i in range(n):
            heapq.heappush(pq, nums[i])
            if len(pq) > k:
                heapq.heappop(pq)
        

        return pq[0]
        