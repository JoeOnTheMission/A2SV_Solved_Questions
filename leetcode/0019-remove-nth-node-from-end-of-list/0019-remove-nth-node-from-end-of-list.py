# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        cur = head
        i = 0
        
        while cur:
            if i < n:#move cur to the right point
                cur = cur.next
                i += 1
            else:
                prev = prev.next
                cur = cur.next
        prev.next = prev.next.next
        return dummy.next