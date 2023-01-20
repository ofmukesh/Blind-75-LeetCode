class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            if n % 2 == 1:
                res += 2 ** (32-i-1)
            n = n >> 1
        
        return (res)
