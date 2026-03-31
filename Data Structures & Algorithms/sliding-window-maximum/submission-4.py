class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        re = [0] * (n-k+1)

        for i in range(n):

            while len(q) > 0 and q[0] <= i-k: q.popleft()
            while len(q) > 0 and nums[q[-1]] <= nums[i]: q.pop()

            q.append(i)

            if i >= k-1:
                re[i-k+1] = nums[q[0]]
        

        return re




        