# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        newDummy = ListNode(0, None)

        ptr = newDummy
        curr1, curr2 = l1, l2
        carry = 0
        while curr1 and curr2:
            val_sum = curr1.val + curr2.val + carry
            val = val_sum % 10
            carry = val_sum // 10
            newNode = ListNode(val, None)
            ptr.next = newNode
            ptr = ptr.next
            curr1 = curr1.next
            curr2 = curr2.next
        
        while curr1:
            val_sum = curr1.val + carry
            val = val_sum % 10
            carry = val_sum // 10
            newNode = ListNode(val, None)
            ptr.next = newNode
            ptr = ptr.next
            curr1 = curr1.next

        while curr2:
            val_sum = curr2.val + carry
            val = val_sum % 10
            carry = val_sum // 10
            newNode = ListNode(val, None)
            ptr.next = newNode
            ptr = ptr.next
            curr2 = curr2.next

        if carry != 0:
            newNode = ListNode(carry, None)
            ptr.next = newNode

        return newDummy.next