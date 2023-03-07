class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0;
        l=0;
        r=len(height)-1;
        while l<r:
            a=(r-l)*min(height[l],height[r]);
            res=max(res,a);

            if height[l]<height[r]:
                l+=1;
            else:
                r-=1;
        return res;

# Explain : We will use index pointing method 
# loop while left is smaller then right index -> find out the area
#                                             -> set ans var to max of (area | itself) [ ^_^ area = width * hieght = (right-left) * min(left ele,right ele) ]
#                                             -> if left index ele < right index ele then move left index to next (+1)
#                                             -> or if right index ele < left index ele then move right index to -1
# after loop return the answer
