class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.res = []
        
        def dfs(i, curCandidates):

            if sum(curCandidates) == target:
                self.res.append(curCandidates.copy())
                return
            
            if i >= len(candidates) or sum(curCandidates) > target:
                return

            # select i
            curCandidates.append(candidates[i])
            dfs(i + 1, curCandidates)
            curCandidates.pop()

            # not select i
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i - 1]:
                i += 1
            dfs(i, curCandidates)

        dfs(0, [])
        return self.res