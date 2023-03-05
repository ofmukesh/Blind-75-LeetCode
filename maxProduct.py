class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # using two variables to store max & min product of current subarray
        min_p,max_p=1,1
        
        # use 3rd variable tostore maxium product of subarrays
        res=max(nums)

        for n in nums:
            
            # if current element is 0 then start with a new subarray
            if n==0:
                min_p=1
                max_p=1
                
            # now updating max_p and min_p with min & max of ele, ele * min_p , ele * max_p
            t=max_p
            max_p=max(n,n*max_p,n*min_p)
            min_p=min(n,n*t,n*min_p)
            
            # updating max product of subarrays
            res=max(min_p,max_p,res)
        return res
   
