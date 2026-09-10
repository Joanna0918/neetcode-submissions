class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodesMap = {n: [] for n in range(n)}
        for n1, n2 in edges:
            nodesMap[n1].append(n2)
            nodesMap[n2].append(n1)

        visit = set()

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for child in nodesMap[node]:
                if child == prev:
                    continue
                if not dfs(child, node):
                    return False 

            return True
        

        if not dfs(0, -1):
            return False
        
        return len(visit) == n