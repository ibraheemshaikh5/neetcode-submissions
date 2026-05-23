# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # edgecases:
            # 1. one list runs out
            # 2. both lists start empty

        # start with a dummy node
        dummy = ListNode()

        # create a tail node
        tail = dummy

        # loop while both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                # if they're less than or equal
                tail.next = list2
                list2 = list2.next
            
            # update tail
            tail = tail.next

        # at this point only one of them will be non-null
        if list1:
            # continue the list for the rest of list1
            tail.next = list1
        elif list2:
            # continue the list for the rest of list2
            tail.next = list2

        # dummy.next is the head
        return dummy.next

