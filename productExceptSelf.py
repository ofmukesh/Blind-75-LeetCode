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

    
# #_Explain
# Create a empty array
# then we have to find product of all left elements of each elements of array except self and add to the new array
# then we have to find product of all rigth elements of each elements of array except self and multiply with same index ele of new array and update the index
# return answers array
