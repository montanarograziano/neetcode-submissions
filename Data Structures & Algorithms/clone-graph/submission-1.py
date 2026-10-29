"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = set()
        d = {}
        
        def dfs(node):
            if node.val in visited or node.val in d:
                return
            visited.add(node.val)
            n = Node(node.val)
            d[node.val] = n
            for nei in node.neighbors:
                n.neighbors = n.neighbors or []
                dfs(nei)
                n.neighbors.append(d[nei.val])

        
        dfs(node)
        return d[1]