# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = deque()
        cur = head
        answer_head = ListNode(None)
        answer = answer_head
        while cur:
            while stack and stack[-1] < cur.val:
                stack.pop()
            stack.append(cur.val)
            cur = cur.next

        cur = head 
        while cur:
            if cur.val == stack[0]:
                answer.next = cur
                answer = answer.next
                stack.popleft()
            
            cur = cur.next
        return answer_head.next
                