
#-------------------------Explainaion-------------------------
# get the sum of the elements 0 to n & the sum of given array 
# the ans is sum(0 to n) - sum(given array)

#-------------------------Code------------------------
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c_sum=0;
        m_sum=0;
        for i in range(len(nums)):
            c_sum+=nums[i];
            m_sum+=i+1;
        return m_sum-c_sum;
    
# same algo we will do like this
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=len(nums);
        for i in range(len(nums)):
            res+=i-nums[i];
        return res;
