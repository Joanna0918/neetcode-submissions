class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        countS, countT = {}, {}

        for c in t:
            countT[c] = countT.get(c, 0) + 1
            countS[c] = 0
        
        match, target = 0, len(countT)
        l, r = 0, 0
        shortest, res = float('inf'), ''
        for r in range(len(s)):
            if s[r] in countS:
                countS[s[r]] += 1
                if countS[s[r]] == countT[s[r]]:
                    match += 1
            
            while match == target:
                if (r - l + 1) < shortest:
                    res = s[l:r+1]
                    shortest = r - l + 1

                if s[l] in countS:
                    countS[s[l]] -= 1
                    if countS[s[l]] < countT[s[l]]:
                        match -= 1
                l += 1

        return res
