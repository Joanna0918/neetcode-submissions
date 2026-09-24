class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longestPrefix = strs[0]

        for s in strs[1:]:
            n = min(len(s), len(longestPrefix))
            i = -1
            while i + 1 < n and s[i + 1] == longestPrefix[i + 1]:
                i += 1
            longestPrefix = longestPrefix[:i + 1] if i != -1 else ""
        
        return longestPrefix
