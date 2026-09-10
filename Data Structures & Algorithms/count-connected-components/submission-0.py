class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodesMap = {node: [] for node in range(n)}
        for n1, n2 in edges:
            nodesMap[n1].append(n2)
            nodesMap[n2].append(n1)

        visit = set()
        def dfs(node, prev):
            if not nodesMap[node] or node in visit:
                return

            visit.add(node)
            for nei in nodesMap[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        
        count = 0
        for i in range(n):
            if i in visit:
                continue
            
            dfs(i, -1)
            count += 1
        
        return count