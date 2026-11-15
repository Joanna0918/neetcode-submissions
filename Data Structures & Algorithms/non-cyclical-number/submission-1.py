class Solution:
    def isHappy(self, n: int) -> bool:
        seen =  set()
        s = str(n)

        while True:
            remain = 0
            for i in s:
                remain += int(i) ** 2
            
            if remain == 1:
                return True
            if remain in seen:
                return False
            seen.add(remain)
            
            s = str(remain)