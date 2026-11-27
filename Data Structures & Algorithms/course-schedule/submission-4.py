class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for c, pre in prerequisites:
            courseMap[c].append(pre)
        
        path = set()
        def dfs(c):
            if c in path:
                return False
            if c not in courseMap:
                return True
            
            path.add(c)
            for p in courseMap[c]:
                if not dfs(p):
                    return False
            path.remove(c)
            courseMap[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True