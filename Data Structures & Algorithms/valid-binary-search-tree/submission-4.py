# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minV, maxV):
            if not root:
                return True

            if not (minV < root.val < maxV):
                return False
            
            l = dfs(root.left, minV, min(maxV, root.val))
            r = dfs(root.right, max(minV, root.val), maxV)
            
            return l and r
        
        return dfs(root, float("-inf"), float("inf"))