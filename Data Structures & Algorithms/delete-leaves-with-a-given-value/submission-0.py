# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(root) -> bool:
            if not root:
                return False
            
            if dfs(root.left):
                root.left = None
            if dfs(root.right):
                root.right = None
            
            return root.val == target and root.left is None and root.right is None
        
        return None if dfs(root) else root