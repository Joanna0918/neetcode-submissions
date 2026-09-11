class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for i in range(n + 1)]

        visit = [False] * (n + 1)
        cycle = set()
        self.cycleStart = -1

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node, prev):
            if visit[node]:
                self.cycleStart = node
                return True
            
            visit[node] = True
            for nei in adj[node]:
                if nei == prev:
                    continue
                if dfs(nei, node):
                    if self.cycleStart != -1:
                        cycle.add(node)
                    if node == self.cycleStart:
                        self.cycleStart = -1
                    return True
            return False
        
        dfs(1, -1)

        for n1, n2 in reversed(edges):
            if n1 in cycle and n2 in cycle:
                return [n1, n2]
        
        return []