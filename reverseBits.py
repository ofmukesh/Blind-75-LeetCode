class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            lsb = n & 1 # getting the least significant bit
            rlsb = lsb << (31-i) 
            res= res | rlsb
            n = n >> 1 # right shifting n by 1
        return (res)
