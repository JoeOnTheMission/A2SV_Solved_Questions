# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1001
        def traveler(node):
            if not node:
                return 
            now = node.val
            left = 0
            right = 0
            if node.left:
                left = traveler(node.left)
                self.res = max(self.res,now + left)
            if node.right:
                right = traveler(node.right)
                self.res = max(self.res,now + right)
            total = now + left + right
            print(left,now,right,total)
            self.res = max(self.res,total,now)

            return max(now + left,now,now + right)
        traveler(root)
        return self.res

        