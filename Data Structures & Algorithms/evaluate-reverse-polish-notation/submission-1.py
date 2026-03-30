class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        st = []
        

        for i in range(n):
            ch = tokens[i]
            print(st)
            
            if ch in ['+', '-', '*', '/']:
                second = st.pop()
                first = st.pop()

                if ch == '+': st.append(first + second)
                elif ch == '-': st.append(first - second)
                elif ch == '*': st.append(first * second)
                elif ch == '/': st.append(int(first / second))
            

            else:
                st.append(int(ch))

        
        return st[-1]


        