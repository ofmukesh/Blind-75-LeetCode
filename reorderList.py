# at first step we will find the second half linked list
# next we will reverse second list
# at last merge first and second half

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head.next
        
        # finding second half using slow fast pointer
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        second=slow.next
        prev=slow.next=None

        # reversing second half
        while second:
            t=second.next
            second.next=prev
            prev=second
            second=t
        
        # merging two halfs
        first=head
        second=prev
        while second:
            t1=first.next
            t2=second.next
            first.next=second
            second.next=t1
            first=t1
            second=t2
