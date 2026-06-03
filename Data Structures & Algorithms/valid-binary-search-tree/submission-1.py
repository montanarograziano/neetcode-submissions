# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        interval = [float('-inf'), float('inf')]

        def dfs(root, interval):
            if not root:
                return True
            
            if root.val <= interval[0] or root.val >= interval[1]:
                return False
        
            return dfs(root.left, [interval[0], root.val]) and dfs(root.right, [root.val, interval[1]])
        
        return dfs(root, interval)