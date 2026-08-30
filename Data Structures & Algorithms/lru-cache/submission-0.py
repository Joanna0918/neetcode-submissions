class Node:

    def __init__(self, key, val, next = None, prev = None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.right, self.left = Node(0, 0), Node(0, 0)
        self.right.prev, self.left.next = self.left, self.right
        self.cache = {}

    
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next, self.right.prev = node, node
        node.prev, node.next = prev, next
    

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            del self.cache[self.left.next.key]
            self.remove(self.left.next)