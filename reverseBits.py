class Solution:
    def reverseBits(self, n: int) -> int:
        x = 0;
        d = 0;
        while(n>0):
            x+=(n%2) << (31-d);
            n >>= 1;
            d+=1;
        return x;
