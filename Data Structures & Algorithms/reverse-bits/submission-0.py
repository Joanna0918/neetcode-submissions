class Solution:
    def reverseBits(self, n: int) -> int:
        binary = ""

        while n > 0 or len(binary) < 32:
            if n == 0:
                binary += "0"
            if n & 1 == 1:
                binary += "1"
            else:
                binary += "0"
            n = n >> 1

        res = 0
        for i in range(32):
            res += int(binary[31-i]) * math.pow(2, i)

        return int(res)