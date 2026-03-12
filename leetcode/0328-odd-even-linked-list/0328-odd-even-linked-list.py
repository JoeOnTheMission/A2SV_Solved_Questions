# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        even_head = ListNode(None)
        even_tail = ListNode(None)
        even = even_head
        cur = head
        last = head
        i = 1
        while cur and cur.next:
            
            temp = cur.next            
           
            cur.next = cur.next.next#remove the even one 
            last = cur
            cur = cur.next

            temp.next = None
            even.next = temp
            
            even = even.next

            
        if cur:
            cur.next = even_head.next
        else:
            last.next = even_head.next
        return head