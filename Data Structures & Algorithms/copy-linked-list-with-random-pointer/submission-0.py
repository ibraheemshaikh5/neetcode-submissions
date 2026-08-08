"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # map each old node to new node in hashmap
        # create basic linked list w/o random - first pass
        # go back through w/ hashmap as a key to add random
        map = {}
        map[None] = None # need to consider the null case
        newDummy = Node(0, None, None)

        curr = head
        newCurr = newDummy
        while curr:
            newNode = Node(curr.val, None, None)
            newCurr.next = newNode
            map[curr] = newNode
            curr = curr.next
            newCurr = newCurr.next
        
        curr = head
        newCurr = newDummy.next
        while curr:
            newCurr.random = map[curr.random]
            curr = curr.next
            newCurr = newCurr.next

        return newDummy.next