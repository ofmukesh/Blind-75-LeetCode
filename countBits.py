class Solution:
    def countBits(self, n: int) -> List[int]:
#         res=[];
#         for i in range(n+1):
#             res.append(bin(i).count('1'));
#         return res;
      
        res=[0 for _ in range(n+1)];
        for i in range(n+1):
            res[i]=res[int(i/2)]+i%2;
        return res; 
