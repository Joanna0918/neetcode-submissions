"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        nodeMap = {}
        newHead = Node(head.val)
        nodeMap[head] = newHead
        curr, newCurr = head, newHead
        while curr:
            if curr.next not in nodeMap:
                if curr.next:
                    nodeMap[curr.next] = Node(curr.next.val)
                else:
                    nodeMap[curr.next] = None
            newCurr.next = nodeMap[curr.next]
            if curr.random not in nodeMap:
                if curr.random:
                    nodeMap[curr.random] = Node(curr.random.val)
                else:
                    nodeMap[curr.random] = None
            newCurr.random = nodeMap[curr.random]

            curr = curr.next
            newCurr = newCurr.next
        
        return newHead
