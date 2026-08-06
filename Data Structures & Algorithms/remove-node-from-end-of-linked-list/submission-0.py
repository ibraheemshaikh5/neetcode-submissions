# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of the linked list
        c = 0
        curr = head
        while curr:
            curr = curr.next
            c += 1

        # iterate until that point
        target = c - n

        if target == 0:
            return head.next
        curr = head
        for i in range(target - 1):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        
        return head