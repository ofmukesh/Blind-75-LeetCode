class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # create a variable to store sum of subarrays (intially-0)
        s=0;
        # create a variable to store maxmium sum of subarrays
        max_sum=nums[0];

        # reach each item in nums
        for num in nums:
            # sum Ith ele of nums and s
            s+=num;
            
            # store max of max_s and s in max_s
            max_sum=max(max_sum,s);
            
            # if sum is less then Zero then set s equal to Zero
            if s<0:
                s=0;
        return max_sum;
        # return max sum of subarray 
    
