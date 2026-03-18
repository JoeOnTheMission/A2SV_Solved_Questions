# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre(self,node):
        if node:
            ans = [node.val]
            left = self.pre(node.left)
            right = self.pre(node.right)
            if left:
                ans.extend(left)
            if right:
                ans.extend(right)
            return ans
        else:
            return []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.pre(root)