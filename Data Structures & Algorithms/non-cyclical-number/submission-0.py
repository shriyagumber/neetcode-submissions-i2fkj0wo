class Solution:
    def isHappy(self, n: int) -> bool:
        self.seen = set()
        return self.check(n)
    
    def check(self, n: int) -> bool:
        if n == 1: return True
        if n in self.seen: return False
        self.seen.add(n)

        curr = 0
        while n > 0:
            mod = n % 10
            curr += mod * mod
            n = n // 10
        
        return self.check(curr)

        