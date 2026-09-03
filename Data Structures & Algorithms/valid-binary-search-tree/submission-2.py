# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lower_bound, upper_bound):
            if not root:
                return True
            
            if lower_bound < root.val and root.val < upper_bound:
                return dfs(root.left, lower_bound, root.val) and dfs(root.right, root.val, upper_bound)
            else:
                return False
        
        return dfs(root, float('-inf'), float('inf'))