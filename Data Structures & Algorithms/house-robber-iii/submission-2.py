from functools import cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        cache = {}
        def dfs(node):
            if not node:
                return 0
            
            if node in cache:
                return cache[node]
            # Option 1: Rob current node + all 4 grandchildren
            rob_curr = node.val
            if node.left:
                rob_curr += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_curr += dfs(node.right.left) + dfs(node.right.right)
            
            # Option 2: Skip current node + rob both children
            skip_curr = dfs(node.left) + dfs(node.right)
            
            cache[node] = max(rob_curr, skip_curr)
            return cache[node]

        return dfs(root)