# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, curr2 = head, head.next
        while curr2 and curr2.next:
            curr = curr.next
            curr2 = curr2.next.next
        head2 = curr.next
        curr.next = None

        # reverse head2
        prev, curr = None, head2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        head2 = prev

        curr, curr2 = head, head2
        while curr and curr2:
            tmp, tmp2 = curr.next, curr2.next
            curr.next = curr2
            curr2.next = tmp
            curr, curr2 = tmp, tmp2
        