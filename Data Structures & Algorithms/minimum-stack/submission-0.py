class MinStack:

    def __init__(self):
        self.st = []
        self.mSt = []
        

    def push(self, val: int) -> None:
        if len(self.mSt) == 0 or self.mSt[-1] >= val:
            self.mSt.append(val)
        else:
            lastMin = self.mSt[-1]
            self.mSt.append(lastMin)
        
        self.st.append(val)
        

    def pop(self) -> None:
        self.st.pop()
        self.mSt.pop()

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.mSt[-1]
        
