class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = bin(n)[2:]
        count = 0

        for i in range(len(bits)):
            if bits[i] == '1': count += 1
        return count
        