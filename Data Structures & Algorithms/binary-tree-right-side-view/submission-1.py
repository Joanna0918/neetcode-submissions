# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        treeList = []
        q = deque()
        if root:
            q.append(root)

        while q:
            levelList = []
            for i in range(len(q)):
                curr = q.popleft()
                levelList.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            treeList.append(levelList)
        
        res = []
        for l in treeList:
            res.append(l.pop())
        return res