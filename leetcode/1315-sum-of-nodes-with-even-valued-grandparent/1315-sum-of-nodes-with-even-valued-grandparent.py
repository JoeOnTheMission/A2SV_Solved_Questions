# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def finder(self,cur,parent = None, grand = None):
        if not cur:
            return 
        
        if grand and grand.val % 2 == 0:
            self.res += cur.val
        self.finder(cur.left,cur,parent)
        self.finder(cur.right,cur,parent)

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.finder(root,None,None)
        return self.res