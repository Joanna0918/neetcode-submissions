class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        res = [0]
        carry = 1
        for d in digits[-2::-1]:
            newD = d + carry
            if newD > 9:
                carry = newD // 10
                newD = newD % 10
                res.append(newD)
            else:
                carry = 0
                res.append(newD)
        if carry != 0:
            res.append(carry)
        res.reverse()
        return res