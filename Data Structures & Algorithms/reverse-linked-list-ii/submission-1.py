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

        # Step 1: Find the start node
        while left > 1:
            before = curr
            curr = curr.next
            left -= 1
        
        # Save the original start (becomes tail after reversal)
        tail = curr

        # Step 2: Reverse the sublist
        prev = None

        for i in range(length):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Reconnect the list
        before.next = prev
        tail.next = curr

        return dummy.next