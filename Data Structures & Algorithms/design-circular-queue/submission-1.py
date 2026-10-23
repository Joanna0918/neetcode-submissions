class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = []
        self.occupied = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue.insert(0, value)
        self.occupied += 1
        return True        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.queue.pop()
        self.occupied -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[-1]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[0]

    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True

    def isFull(self) -> bool:
        return self.occupied == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()