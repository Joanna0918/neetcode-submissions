class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = defaultdict(list)

        for s in strs:
            sArray = [0] * 26
            for c in s:
                sArray[ord(c) - ord('a')] += 1
            strsMap[tuple(sArray)].append(s)

        return list(strsMap.values())