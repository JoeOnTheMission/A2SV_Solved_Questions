# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,node,res):
        if node:
            self.pre(node.left,res)
            res.append(node.val)
            self.pre(node.right,res)
            return res
        else:
            return res
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.pre(root,[])