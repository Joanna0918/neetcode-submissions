class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1Map, s2Map = {}, {}
        
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        for l in range(len(s2)):
            r = l + window - 1
            if r > len(s2)-1:
                return False

            if not s2Map:
                for c in s2[l:r]:
                    s2Map[c] = s2Map.get(c, 0) + 1

            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1

            if s1Map == s2Map:
                return True
            else:
                s2Map[s2[l]] = s2Map.get(s2[l]) - 1
            
            if s2Map[s2[l]] == 0:
                del s2Map[s2[l]]
        
        return False