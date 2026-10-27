# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, left, right):
            if not root:
                return
            
            if not (left < root.val < right):
                self.res = False
            
            if root.left:
                dfs(root.left, left, root.val)
            if root.right:
                dfs(root.right, root.val, right)
            
        
        dfs(root, float("-inf"), float("inf"))

        return self.res