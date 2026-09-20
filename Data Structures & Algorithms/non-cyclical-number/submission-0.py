class Solution:
    def isHappy(self, n: int) -> bool:
        s = str(n)
        seen = set()

        while True:
            new = 0

            for i in s:
                new += int(i) ** 2

            if new == 1:
                return True

            if new in seen:
                return False

            seen.add(new)
            s = str(new)