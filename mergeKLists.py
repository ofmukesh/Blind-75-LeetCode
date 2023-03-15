# Explain :- we will simply merge 2 lists and then next two lists and so on & with this we will store the merged lists to in lists , and again we will do the same proccess while lists not have only one merge sorted list 

# ------------------code-----------------
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # return empty or None if lists have no element
        if not lists or len(lists)==0:
            return None
        
        # loop while lists len is not less than 1
        while len(lists)>1:
            # temp merged list
            mergedLists=[]

            # sort 2 lists per round 
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1 < len(lists) else None
                # merge two list and add the merged list to the mergedLists array 
                mergedLists.append(self.merge(l1,l2))

            # store new merged sorted lists to lists
            lists=mergedLists
        
        # return the sorted merged list of lists 😉
        return lists[0]

    # simple merge sorted list algorithm, we have already done in (21. Merge Two Sorted Lists)
    def merge(self,l1,l2):
        dummy=ListNode()
        new=dummy

        while l1 and l2:
            if l1.val>l2.val:
                new.next=l2
                l2=l2.next
            else:
                new.next=l1
                l1=l1.next
            new=new.next
        
        if not l1:
            new.next=l2
        elif not l2:
            new.next=l1
        
        return dummy.next
