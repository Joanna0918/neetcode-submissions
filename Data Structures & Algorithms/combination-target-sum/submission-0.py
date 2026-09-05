class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []

        def dfs(i, node):
            if sum(node.val) == target:
                self.res.append(node.val)
            elif sum(node.val) > target or i >= len(nums):
                return
            else:
                node.left = TreeNode(node.val + [nums[i]])
                node.right = TreeNode(node.val)

                dfs(i, node.left)
                dfs(i + 1, node.right)
        
        dfs(0, TreeNode([]))
        return self.res