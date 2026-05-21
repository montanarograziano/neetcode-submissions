class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True
        nodes = defaultdict(list)
        for e1, e2 in edges:
            nodes[e1].append(e2)
            nodes[e2].append(e1)
        
        visit = set()

        def dfs(node):
            if node in visit:
                return

            visit.add(node)
            for n in nodes[node]:
                dfs(n)
        
        dfs(0)
        return len(edges) == (n - 1) and len(visit) == n

        
