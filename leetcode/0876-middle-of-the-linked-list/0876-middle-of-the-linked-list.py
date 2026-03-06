# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        cur = head
        while True:
            if cur.next:
                cur = cur.next.next
                middle = middle.next
            if not cur:
                return middle
            elif not cur.next:
                return middle


        