# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        curr = newList
        currList1, currList2 = list1, list2

        while currList1 or currList2:
            if currList1 and (not currList2 or currList1.val <= currList2.val):
                curr.next = currList1
                currList1 = currList1.next
            else:
                curr.next = currList2
                currList2 = currList2.next
            curr = curr.next
        
        return newList.next