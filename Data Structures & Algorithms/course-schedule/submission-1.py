class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for c, pre in prerequisites:
            courseMap[c].append(pre)
        
        path = set()
        visited = set()

        def dfs(c):
            if c in path:
                return False
            if c not in courseMap or c in visited:
                return True

            path.add(c)
            for preCourse in courseMap[c]:
                if not dfs(preCourse):
                    return False
            path.remove(c)

            visited.add(c)
            return True
        
        for c in courseMap:
            if not dfs(c):
                return False
        return True