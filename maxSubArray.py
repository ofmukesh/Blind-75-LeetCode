class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0;
        max_sum=nums[0];

        for num in nums:
            s+=num;
            max_sum=max(max_sum,s);
            if s<0:
                s=0;
        return max_sum;
