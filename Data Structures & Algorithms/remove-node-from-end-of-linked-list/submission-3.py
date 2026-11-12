# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeMap = {}
        dummy = ListNode()
        dummy.next = head
        curr = dummy
        number = 0
        while curr:
            nodeMap[number] = curr
            number += 1
            curr = curr.next

        n_1_node = nodeMap[number - 1 - n]
        n_1_node.next = n_1_node.next.next
        return dummy.next