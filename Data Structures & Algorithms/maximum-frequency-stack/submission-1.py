class FreqStack:

    def __init__(self):
        self.count = defaultdict(int)
        self.maxCnt = 0
        self.stacks = defaultdict(list)

    def push(self, val: int) -> None:
        self.count[val] += 1
        if self.count[val] > self.maxCnt:
            self.maxCnt = self.count[val]
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.count[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()