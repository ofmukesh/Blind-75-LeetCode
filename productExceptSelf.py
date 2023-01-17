class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        o=[1]*(len(nums));

        p=1;
        for i in range(len(nums)):
            o[i]=p;
            p*=nums[i];
            
        p=1;
        for i in range(len(nums)-1,-1,-1):
            o[i]*=p;
            p*=nums[i];

        return o;
