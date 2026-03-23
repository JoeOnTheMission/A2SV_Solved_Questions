# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def finder(self,cur,parent = None, grand = None):
        if not cur:
            return 0
        total = 0
        if grand and grand.val % 2 == 0:
            total += cur.val
        total += self.finder(cur.left,cur,parent)
        total += self.finder(cur.right,cur,parent)
        return total


    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.finder(root,None,None)