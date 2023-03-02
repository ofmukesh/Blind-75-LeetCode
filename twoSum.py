class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Psuedocode
            # Create a empty hashmap 
            # check target-current_ele is exist in hashmap or not
            # if exist - return current index & hashmap key's value
            # else add current ele as key & its index as value
        
        hsh={}
        for index,ele in enumerate(arr):
            r = target-ele
            if hsh.get(r) != None:
                print([hsh.get(r),index])
                break;
            else:
                hsh[ele]=index
