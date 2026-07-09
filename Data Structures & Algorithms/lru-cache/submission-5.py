class Node:
    def __init__(self, key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.hm = {}
        self.head, self.tail = Node(0,0),  Node(0,0)
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.hm.get(key, None)

        if node is None:
            return -1
        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev

        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.hm.get(key, None)

        if node is None:
            node = Node(key, value)
            self.hm[key] = node

        else:
            prev = node.prev
            nxt = node.next
            prev.next = nxt
            nxt.prev = prev
            node.val = value

        
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
        
        if len(self.hm) > self.capacity:
            lru = self.tail.prev
            prev = lru.prev
            prev.next = self.tail
            self.tail.prev = prev
            del self.hm[lru.key]