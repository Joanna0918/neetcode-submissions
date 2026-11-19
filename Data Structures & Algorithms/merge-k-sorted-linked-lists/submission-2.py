# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                if i + 1 == len(lists):
                    mergedLists.append(lists[i])
                    break

                l1, l2 = lists[i], lists[i + 1]
                dummy = ListNode()
                curr = dummy
                while l1 or l2:
                    if l1 and l2:
                        if l1.val < l2.val:
                            curr.next = l1
                            l1 = l1.next
                        else:
                            curr.next = l2
                            l2 = l2.next
                    elif l1:
                        curr.next = l1
                        break
                    elif l2:
                        curr.next = l2
                        break
                    curr = curr.next
                mergedLists.append(dummy.next)
            lists = mergedLists
        
        return lists[0] if lists else None