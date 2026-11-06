class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minL = float("inf")
        for s in strs:
            minL = min(minL, len(s))
            if len(s) == minL:
                prefix = s
        
        for i in range(minL):
            for s in strs:
                if s[i] != prefix[i]:
                    return prefix[:i]
        return prefix