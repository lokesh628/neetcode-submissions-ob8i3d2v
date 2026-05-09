# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        prev=None
        curr=head
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        curr=prev
        i=0
        while curr:
            if curr.val!=arr[i]:
                return False
            curr=curr.next
            i+=1
        return True
