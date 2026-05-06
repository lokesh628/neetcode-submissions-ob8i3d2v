# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==0:
            return head
        curr=head
        n=0
        while curr:
            curr=curr.next
            n+=1
        k=k%n
        newcurr=head
        while newcurr.next:
            newcurr=newcurr.next
        newcurr.next=head
        tail=head
        for i in range(n-k-1):
            tail=tail.next
        newhead=tail.next
        tail.next=None
        return newhead
