# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def dfs(root, cur: int) -> int:
            if not root:
                return cur
            
            cur += 1
            left, right = 0, 0
            if root.left:
                left = dfs(root.left, cur)
            if root.right:
                right = dfs(root.right, cur)
            
            return max(cur, left, right)
        
        return dfs(root, 0)
