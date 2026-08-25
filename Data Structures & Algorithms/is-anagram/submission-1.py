class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = {}
        for cha in s:
            if cha not in sMap:
                sMap[cha] = 1
            else:
                sMap[cha] += 1
        
        tMap = {}
        for cha in t:
            if cha not in tMap:
                tMap[cha] = 1
            else:
                tMap[cha] += 1
        
        if len(sMap) == len(tMap):
            for k in sMap:
                if k not in tMap or sMap[k] != tMap[k]:
                    return False
        else:
            return False
        
        return True