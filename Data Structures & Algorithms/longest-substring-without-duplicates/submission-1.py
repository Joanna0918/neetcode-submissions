class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1

        res = 1
        l, r = 0, 1
        seen = set(s[l])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            res = max(res, r - l + 1)
            seen.add(s[r])
            r += 1
        
        return res