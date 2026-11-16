class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        s1Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1
        
        i = 0
        while i < n2:
            if s2[i] in s1Count:
                j = i
                s2Count = defaultdict(int)
                while j < n2 and j - i + 1 <= n2:
                    if s2[j] not in s1Count:
                        break
                    s2Count[s2[j]] += 1
                    if s1Count == s2Count:
                        return True
                    if s2Count[s2[j]] > s1Count[s2[j]]:
                        break
                    j += 1
            i += 1
        return False