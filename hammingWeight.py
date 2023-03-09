class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        #2 We will remove 1 using AND operator and count how many times 1`s removed and return it
        while n:
            n &= (n-1)
            res += 1

        #2 Basically we were doing here is cheking last bit is 0 or 1 then right shifting given integer
        # while n:
        #     res += (n % 2)
        #     n=n>>1
        
        return res


#Time compexity O(32) > O(1)
#Space compexity O(1)
