class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ""
        for i in range(1, n+1):
            res += str(bin(i))[2:] # because returns 0b{binary_digit}
        
        return int(res, 2) % (10**9 + 7)