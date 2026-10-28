# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = -1
    cnt = -1
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            self.cnt -= 1
            print(self.cnt, root.val)

            if self.cnt == 0:
                self.res = root.val
                return
            
            dfs(root.right)
        
        dfs(root)
        return self.res
            
