# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checker(self, cur1, cur2):
        if not self.valid:
            return
        
        if not cur1 and not cur2:
            return
        if not cur1 or not cur2:
            self.valid = False
            return

        if cur1.val != cur2.val:
            self.valid = False
            return

        self.checker(cur1.left, cur2.left)
        self.checker(cur1.right, cur2.right)

    def traverser(self, cur):
        if self.done:
            return
        if not cur:
            return

        if cur.val == self.head.val:  # FIXED
            self.valid = True
            self.checker(cur, self.head)
            if self.valid:
                self.done = True
                return

        self.traverser(cur.left)
        self.traverser(cur.right)

    def isSubtree(self, root, subRoot):
        self.head = subRoot
        self.done = False
        self.traverser(root)
        return self.done