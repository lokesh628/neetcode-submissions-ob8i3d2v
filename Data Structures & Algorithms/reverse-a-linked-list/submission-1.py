# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        arr1=arr[::-1]
        newcurr=ListNode(arr1[0])
        curr=newcurr
        for i in range(1,len(arr1)):
            curr.next=ListNode(arr1[i])
            curr=curr.next
        return newcurr