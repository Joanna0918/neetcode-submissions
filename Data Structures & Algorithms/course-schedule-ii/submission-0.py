class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        completed = set()
        coursePre = {c: [] for c in range(numCourses)}

        for c, p in prerequisites:
            coursePre[c].append(p)
        
        res = []

        def dfs(c):
            if c in visit:
                return False
            if c in completed:
                return True
            
            visit.add(c)
            for pre in coursePre[c]:
                if not dfs(pre):
                    return False
            visit.remove(c)
            completed.add(c)
            res.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return res