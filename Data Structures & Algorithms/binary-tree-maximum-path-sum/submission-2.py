# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = root.val

        def dfs(root):
            if not root:
                return 0
            
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)

            self.res = max(self.res, leftSum + rightSum + root.val)
            
            if not root.left and not root.right:
                return max(0, root.val)
            else:
                return root.val + max(0, leftSum, rightSum)
        
        dfs(root)
        return self.res