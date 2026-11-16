class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        remain = 1
        for n in digits[::-1]:
            new = (n + remain) % 10
            remain = (n + remain) // 10
            res.append(new)
        if remain > 0:
            res.append(remain)
        return res[::-1]