# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # process:
        # first find the first node of the new list
        # set that as a new node
        # then use a pointer to keep adding to the new linked list
        # repeat this while there are still nodes in list1 and list2


        # find first value
        if not list1 and not list2:
            return None
        elif list1 and list2:
            if list1.val <= list2.val:
                newHead = list1
                list1 = list1.next
            elif list2.val < list1.val:
                newHead = list2
                list2 = list2.next
            
            
        # failsafe to ensure variables exist if only one
        # list is populated
        elif list1 and not list2:
            newHead = list1
            list1 = list1.next
        elif list2 and not list1:
            newHead = list2
            list2 = list2.next

        curr = newHead

        while list1 and list2:
            # check incase end of either list has been reached
            if not list1:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            elif not list2:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif list1.val < list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            elif list2.val < list1.val:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            elif list1.val == list2.val:
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                curr.next = list2
                list2 = list2.next
                curr = curr.next

        if not list1 and list2:
            while list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next 
        
        if not list2 and list1:
            while list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next

        return newHead

# time complexity O(n)
# memory O(1)