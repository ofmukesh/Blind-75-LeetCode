class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0];
        else:
            l=0;
            h=len(nums)-1;
            
            while l <= h:
                mid=int((l+h)/2);
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1];
                elif nums[mid] < nums[mid-1]:
                    return nums[mid];
                elif nums[l] <= nums[mid]:
                    l=mid+1;
                elif nums[mid] <= nums[h]:
                    h=mid-1;
             
