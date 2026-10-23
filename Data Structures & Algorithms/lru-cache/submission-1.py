class Node:
    def __init__(self, key = None, val = None, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRUMap = {}
        self.head = Node()
        self.tail = Node(None, None, self.head, None)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.LRUMap:
            curr = self.LRUMap[key]
            curr.prev.next = curr.next
            curr.next.prev = curr.prev

            temp = self.tail.prev
            self.tail.prev = curr
            curr.next = self.tail
            curr.prev = temp
            temp.next = curr
            return curr.val
        
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.tail.prev.val = value
            return
        
        if len(self.LRUMap) == self.capacity:
            remove = self.head.next
            self.head.next = self.head.next.next
            self.head.next.prev = self.head

            del self.LRUMap[remove.key]
        
        curr = Node(key, value)
        prev = self.tail.prev
        self.tail.prev = curr
        prev.next = curr
        curr.next = self.tail
        curr.prev = prev

        self.LRUMap[key] = curr
