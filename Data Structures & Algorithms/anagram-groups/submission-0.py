class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        resultMap = {}

        for s in strs:
            sorted_s = str(sorted(s))
            if sorted_s not in resultMap:
                resultMap[sorted_s] = [s]
            else:
                resultMap[sorted_s] += [s]
        
        result = []

        for i in resultMap:
            result.append(resultMap[i])

        return result