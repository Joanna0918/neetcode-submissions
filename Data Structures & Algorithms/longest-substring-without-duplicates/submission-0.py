class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        res = 1
        l, r = 0, 1
        tempSet = {s[l]}

        while r < len(s):
            while s[r] in tempSet:
                tempSet.remove(s[l])
                l += 1
            
            tempSet.add(s[r])
            res = max(res, len(tempSet))
            r += 1
        
        return res