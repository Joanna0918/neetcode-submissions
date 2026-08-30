# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        reversed_list, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = reversed_list
            reversed_list = curr
            curr = tmp
        
        prev, curr = None, reversed_list
        for i in range(n):
            if i == n-1:
                if prev is None:
                    reversed_list = curr.next
                else:
                    prev.next = curr.next
            prev = curr
            curr = curr.next
        
        res_list, curr = None, reversed_list
        while curr:
            tmp = curr.next
            curr.next = res_list
            res_list = curr
            curr = tmp
        
        return res_list