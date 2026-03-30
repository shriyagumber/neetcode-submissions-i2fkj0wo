class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = []

        for i in range(n):
            ch = s[i]

            if ch == '(': st.append(')')
            elif ch == '[': st.append(']')
            elif ch == '{': st.append('}')
            elif len(st) == 0 or st[-1] != ch: return False
            else: st.pop()
        
        return len(st) == 0
        