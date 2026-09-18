class Solution:
    def countBinaryBits(self, n):
        count = 0
        while n > 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count
        
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            res.append(self.countBinaryBits(i))
        return res