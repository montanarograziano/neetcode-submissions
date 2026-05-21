class Solution:
    total = 0
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        
        visit = set()
        def dfs(node, prev):
            if node in visit:
                return
            
            if prev == -1:
                self.total += 1
            
            visit.add(node)
            for neigh in graph[node]:
                dfs(neigh, node)
        
        for node in graph:
            dfs(node, -1)
        
        return self.total
