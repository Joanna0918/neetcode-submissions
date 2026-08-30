# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        currRes = res
        currL1, currL2 = l1, l2

        while currL1 or currL2:
            if not currL1:
                currL1 = ListNode(0)
            if not currL2:
                currL2 = ListNode(0)

            resVal = currRes.val + currL1.val + currL2.val
            if resVal >= 10:
                currRes.val = resVal - 10
                currRes.next = ListNode(1)
            else:
                currRes.val = resVal
                # Only create next node if more digits remain
                if currL1.next or currL2.next:
                    currRes.next = ListNode(0)
            
            currL1, currL2 = currL1.next, currL2.next
            currRes = currRes.next
        
        return res