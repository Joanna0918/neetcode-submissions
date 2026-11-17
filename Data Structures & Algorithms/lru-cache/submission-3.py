class LinkedListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        self.head = LinkedListNode()
        self.tail = LinkedListNode()

        self.head.next = self.tail
        self.tail.prev = self.head


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoubleLinkedList()

        # key -> node
        self.store = {}

    def removeNode(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    def addToTail(self, node):
        prev = self.cache.tail.prev

        prev.next = node
        node.prev = prev

        node.next = self.cache.tail
        self.cache.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1

        node = self.store[key]

        # Move accessed node to MRU position
        self.removeNode(node)
        self.addToTail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            node = self.store[key]

            node.val = value

            self.removeNode(node)
            self.addToTail(node)

            return

        newNode = LinkedListNode(key, value)

        self.store[key] = newNode
        self.addToTail(newNode)

        if len(self.store) > self.capacity:
            # Remove LRU
            removeNode = self.cache.head.next

            self.removeNode(removeNode)
            del self.store[removeNode.key]