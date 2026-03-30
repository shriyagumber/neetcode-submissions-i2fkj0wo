class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        carry = 1
        for i in range(n-1,-1,-1):
            digits[i] += carry
            carry = int(digits[i] / 10)
            digits[i] = digits[i] % 10

            if carry == 0: break

        if carry > 0:
            re = [0] * (n+1)
            re[0] = 1
            return re
        
        return digits
        