class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            if digits[i] != 9: break
            
            if i == n-1 and digits[i] == 9:
                re = [0] * (n+1)
                re[0] = 1
                return re
        

        carry = 1
        for i in range(n-1,-1,-1):
            digits[i] += carry
            carry = int(digits[i] / 10)
            digits[i] = digits[i] % 10

            if carry == 0: break

        return digits
        