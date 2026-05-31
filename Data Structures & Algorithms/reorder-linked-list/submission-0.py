# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        n=len(arr)
        l=[]
        i,j=0,len(arr)-1
        while i<j:
            l.append(arr[i])
            l.append(arr[j])
            i+=1
            j-=1
        if i==j:
            l.append(arr[i])
        curr=head
        i=0
        while curr:
            curr.val=l[i]
            curr=curr.next
            i+=1
        return
        
        