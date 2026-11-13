class Solution:
    def hammingWeight(self, n: int) -> int:
        biexp = ""
        remain = n
        while remain:
            mod = str(remain % 2)
            remain = remain // 2
            biexp = mod + biexp
        
        res = 0
        for b in biexp:
            if b == "1":
                res += 1
        return res