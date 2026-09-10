class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit = set()
        coursePre = defaultdict(list)

        for c in range(numCourses):
            coursePre[c] = []
        for c, p in prerequisites:
            coursePre[c].append(p)
        
        def dfs(c):
            if c in visit:
                return False
            if not coursePre[c]:
                return True
            
            visit.add(c)
            for preC in coursePre[c]:
                if not dfs(preC):
                    return False
            visit.remove(c)

            coursePre[c] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True