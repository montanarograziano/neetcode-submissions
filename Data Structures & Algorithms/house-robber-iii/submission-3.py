class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, skip)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob = node.val + left[1] + right[1]
            skip = max(left) + max(right)
            
            return (rob, skip)

        return max(dfs(root))