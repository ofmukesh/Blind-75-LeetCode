# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Example: If you have 1->2->3->4->null
# solution: step by step proccess
#            prev = null,                  head = 1->2->3->4->null
#            prev = 1->null,               head = 2->3->4->null
#            prev = 2->1->null,            head = 3->4->null
#            prev = 3->2->1->null,         head = 4->null
#            prev = 4->3->2->1->null,      head = null

# let's code the algo
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # previous node (None at start)
        prev=None

        # loop while head is not null 
        while head:
            # head = 1->2->3->4->null
            # saving the next of current node to temp_next ( temp_next=2->3->4->null ) 
            temp_next=head.next 

            # updating next of current node to prev ( head=1->None )
            head.next=prev

            # updating prev to new current node ( prev=1->None )
            prev=head

            # set the current node to temp_next node ( head=2->3->4->null )
            head=temp_next

        # return the prev node (4->3->2->1->None)
        return prev


# Time complexity - O(n)
# Space complexity - O(n)
