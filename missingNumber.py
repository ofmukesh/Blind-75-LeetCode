class Solution:
    #my solution
    def missingNumber(self, nums: List[int]) -> int:
        c_sum=0;
        m_sum=0;
        for i in range(len(nums)):
            c_sum+=nums[i];
            m_sum+=i+1;
        return m_sum-c_sum;
      
      
    #others solution
#     def missingNumber(self, nums: List[int]) -> int:
#         res=0;
#         for i in range(len(nums)):
#             res=res+i+1-nums[i];
#         return res;
