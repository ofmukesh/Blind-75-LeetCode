class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return first element if array is sorted and 0 times rotated
        if nums[0]<nums[-1] or len(nums)==1:
            return nums[0];
        else:
            # variable for pointing left index
            l=0
            
            # variable for pointing right index
            h=len(nums)-1;
            
            # finding min ele of array
            while l <= h:
                
                # middel element index
                mid=int((l+h)/2);
                
                # return next ele of mid if next ele is not greater then mid
                if nums[mid] > nums[mid+1]:
                    return nums[mid+1];
                # return previous ele of mid if prev ele is greater then mid
                elif nums[mid] < nums[mid-1]:
                    return nums[mid];
                
                # move left to middle+1 ele if left - mid indexe elements is sorted
                elif nums[l] <= nums[mid]:
                    l=mid+1;
                # move right to middle-1 ele if mid-right indexe elements is sorted
                elif nums[mid] <= nums[h]:
                    h=mid-1;
             
