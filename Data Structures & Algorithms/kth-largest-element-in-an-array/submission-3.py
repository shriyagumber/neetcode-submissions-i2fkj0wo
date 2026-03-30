class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pq = []

        for i in range(n):
            if len(pq) == k and nums[i] < pq[0]: continue
            heapq.heappush(pq, nums[i])
            if len(pq) > k:
                heapq.heappop(pq)
        
        return pq[0]
        