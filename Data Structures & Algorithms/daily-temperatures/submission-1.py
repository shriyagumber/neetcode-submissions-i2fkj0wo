class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        re = [0] * n

        st = []

        for i in range(n):
            while st and temperatures[st[-1]] < temperatures[i]:
                idx = st[-1]
                re[idx] = i - idx
                st.pop()
            
            st.append(i)
        
        return re

        