# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, max):
            if not root:
                return None
            
            if root.val >= max:
                self.res += 1
                max = root.val

            dfs(root.left, max)
            dfs(root.right, max)
        
        dfs(root, root.val - 1)
        return self.res
