# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, cur):
            nonlocal res
            if not root:
                return
            
            if cur <= root.val:
                res += 1
            
            if root.left:
                dfs(root.left, max(cur, root.val))

            if root.right:
                dfs(root.right, max(cur, root.val))


        dfs(root, root.val)
        return res

