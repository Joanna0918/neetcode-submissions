class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        minL, resL, resR = float("inf"), 0, 0
        sCount, tCount, tSet = {}, {}, set()

        for c in t:
            tCount[c] = tCount.get(c, 0) + 1
            tSet.add(c)
        
        l, r = 0, 0
        while r < len(s):
            sCount[s[r]] = sCount.get(s[r], 0) + 1
            if s[r] in tCount and sCount[s[r]] >= tCount[s[r]] and s[r] in tSet:
                tSet.remove(s[r])
            r += 1

            while not tSet:
                if r - l < minL:
                    minL = r - l
                    resL, resR = l, r
                if s[l] in tCount and sCount[s[l]] == tCount[s[l]]:
                    tSet.add(s[l])
                sCount[s[l]] -= 1
                l += 1

        return s[resL : resR]