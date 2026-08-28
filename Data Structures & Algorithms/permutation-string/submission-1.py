class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        s1Map = {}
        
        for c in s1:
            s1Map[c] = s1Map.get(c, 0) + 1

        for l in range(len(s2)):
            s2Map = {}
            r = l + window - 1
            if r > len(s2)-1:
                return False
            
            if s2[l] in s1Map:
                for c in s2[l:(r+1)]:
                    s2Map[c] = s2Map.get(c, 0) + 1
                if s1Map == s2Map:
                    return True
            else:
                continue
        
        return False