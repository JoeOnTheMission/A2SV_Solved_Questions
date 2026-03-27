# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverser(self,cur):
        if not cur or self.found:
            return 
        #is this the second num:
        if cur.val in self.needed:
            self.found = True
            return
        #add to needed
        self.needed.add(self.target - cur.val)
        # got to left then right
        if cur.left:
            self.traverser(cur.left)
        if cur.right:
            self.traverser(cur.right)


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.needed = set()
        self.found = False
        self.target = k
        self.traverser(root)
        return self.found