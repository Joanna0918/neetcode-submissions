class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
        
        i, lastI = 0, lastIndex[s[0]]
        size, res = 1, []
        while i < len(s):
            if i == lastI:
                res.append(size)
                size = 1
                i += 1
                lastI = lastIndex[s[i]] if i < len(s) else i
                continue

            lastI = max(lastIndex[s[i]], lastI)
            i += 1
            size += 1
        
        return res

