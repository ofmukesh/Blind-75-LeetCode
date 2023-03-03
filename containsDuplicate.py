class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set={}

        for ele in nums:
            if hash_set.get(ele)==None:
                hash_set[ele]=1
            else:
                return True
        return False;
    
    
#_Explain
#create a empty hash_set
#pick up each elements of array one by one & check :-
#   if element exist in hash_set -> return True
#   and if element not exist in hash_set -> add element to hash_set
#   if no one element is same then return False
