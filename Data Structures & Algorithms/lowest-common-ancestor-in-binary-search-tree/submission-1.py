# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return  
            a, b = (p, q) if p.val < q.val else (q, p)
            
            if a.val < node.val and b.val < node.val and node.left:
                return dfs(node.left)
            
            if a.val > node.val and b.val > node.val and node.right:
                return dfs(node.right)
            
            return node
            
        

        return dfs(root)
