# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestorP, ancestorQ = [], []

        # find p
        curr = root
        while curr != p:
            ancestorP.append(curr)
            
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right
        ancestorP.append(curr) # node itself is its ancestor

        # find q
        curr = root
        while curr != q:
            ancestorQ.append(curr)
            
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
        ancestorQ.append(curr) # node itself is its ancestor

        l = min(len(ancestorP), len(ancestorQ))
        ancestorP, ancestorQ = ancestorP[0:l], ancestorQ[0:l]

        for i in range(l-1, -1, -1):
            if ancestorP[i] == ancestorQ[i]:
                return ancestorP[i]