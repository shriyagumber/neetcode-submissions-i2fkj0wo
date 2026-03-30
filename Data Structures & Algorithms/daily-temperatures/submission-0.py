class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        re = [0] * n

        st = []

        for i in range(n):
            while len(st) > 0 and temperatures[st[-1]] < temperatures[i]:
                re[st[-1]] = i - st[-1]
                st.pop()
            
            st.append(i)
        
        return re

        