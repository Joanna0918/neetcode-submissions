# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        check = head
        while check:
            n += 1
            check = check.next

        list1, split = head, head

        for i in range(math.ceil(n/2)-1):
            split = split.next
        list2 = split.next
        split.next = None

        # reverse list2
        prev, curr = None, list2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        reversed_list2 = prev

        # merge list1 and list2
        while reversed_list2:
            nxt_list1, nxt_list2 = list1.next, reversed_list2.next
            list1.next = reversed_list2
            reversed_list2.next = nxt_list1

            list1 = nxt_list1
            reversed_list2 = nxt_list2
