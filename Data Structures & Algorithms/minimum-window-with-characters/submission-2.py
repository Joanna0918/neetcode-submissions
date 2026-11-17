class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, resLen = "", len(s) + len(t)
        tCount = Counter(t)
        sCount = defaultdict(int)
        need, have = len(tCount), 0

        l = 0
        for r in range(len(s)):
            sCount[s[r]] += 1
            if s[r] in tCount and sCount[s[r]] == tCount[s[r]]:
                have += 1
            
            while l <= r and have == need:
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = s[l : r + 1]
                
                sCount[s[l]] -= 1
                if sCount[s[l]] == 0:
                    del sCount[s[l]]
                
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    have -= 1
                
                l += 1

        return res if resLen < (len(s) + len(t)) else ""