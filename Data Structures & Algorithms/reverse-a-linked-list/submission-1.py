# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set up variables
        curr, prev = head, None

        # run until current is None
        while curr:
            # store address of next node forwards
            temp = curr.next

            # reverse node direction
            curr.next = prev

            # move prev up
            prev = curr

            # move curr up
            curr = temp

        return prev
