class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ls, lt = [0] * 26, [0] * 26
        for i in range(len(s)):
            ls[ord(s[i]) - ord('a')] += 1
            lt[ord(t[i]) - ord('a')] += 1
        
        return ls == lt