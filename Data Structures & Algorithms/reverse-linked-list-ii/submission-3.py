# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        length = right - left + 1
        dummy = ListNode(0, head)
        before, curr = dummy, head

        while left > 1:
            before = curr
            curr = curr.next
            left -= 1
        
        tail = curr
        prev = None
        for i in range(length):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        before.next = prev
        tail.next = curr

        return dummy.next