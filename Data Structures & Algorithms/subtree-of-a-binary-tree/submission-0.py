# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q) -> bool:
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False
        
        def dfs(node) -> bool:
            if not node:
                return
            cur = sameTree(node, subRoot)
            left, right = False, False
            if cur:
                return True
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            return left or right

        
        return dfs(root)
