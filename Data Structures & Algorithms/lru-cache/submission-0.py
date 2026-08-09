# write a node class
class Node:
    def __init__(self, key, val, prev, next):
        self.key, self.val = key, val
        self.prev, self.next = prev, next


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key points to a node(key, val)

        self.cap = capacity
        
        # nodes for left and right pointers
        self.lru = Node(0, 0, None, None)
        self.mru = Node(0, 0, None, None)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    # add helper funcs to rmv/insert using ll
    def rmv(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        # always put it on the rightmost side (MRU)
        prev, nxt = self.mru.prev, self.mru
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.rmv(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.rmv(self.cache[key])
        
        self.cache[key] = Node(key, value, None, None)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru_node = self.lru.next
            self.rmv(lru_node)
            del self.cache[lru_node.key]