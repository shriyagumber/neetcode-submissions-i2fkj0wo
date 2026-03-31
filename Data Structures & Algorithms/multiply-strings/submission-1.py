class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)

        val1 = 0
        for i in range(m):
            curr = ord(num1[i]) - ord('0')
            val1 = val1 * 10 + curr

        val2 = 0
        for i in range(n):
            curr = ord(num2[i]) - ord('0')
            val2 = val2 * 10 + curr
        
        return str(val1 * val2)