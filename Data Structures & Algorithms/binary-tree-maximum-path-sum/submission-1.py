class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # Base case:
            # - branch sum is 0 (contributes nothing to a parent path)
            # - overall max is -inf (handles trees with only negative values)
            if not node:
                return 0, float('-inf')
            
            left_branch, left_overall = dfs(node.left)
            right_branch, right_overall = dfs(node.right)
            
            # If a child's branch sum is negative, ignore it (take 0)
            left_gain = max(0, left_branch)
            right_gain = max(0, right_branch)
            
            # 1. Best single branch path extending down from this node
            current_branch = node.val + max(left_gain, right_gain)
            
            # 2. Path splitting at the current node
            current_split = node.val + left_gain + right_gain
            
            # 3. Best overall path seen in this entire subtree
            current_overall = max(current_split, left_overall, right_overall)
            
            return current_branch, current_overall

        # Return the overall maximum found across the entire tree
        return dfs(root)[1]