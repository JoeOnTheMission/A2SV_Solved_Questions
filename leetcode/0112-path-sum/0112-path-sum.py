# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,cur):
        #print(self.cur_sum,self.target)
        if self.found:
            return 
        
        if not cur:
            return
        
        if cur.left:
            self.cur_sum += cur.left.val
            self.dfs(cur.left)
            self.cur_sum -= cur.left.val
        if cur.right:
            self.cur_sum += cur.right.val
            self.dfs(cur.right)
            self.cur_sum -= cur.right.val
        if not cur.left and not cur.right:
            if self.cur_sum == self.target:
                self.found = True


            

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        self.cur_sum = root.val
        self.target = targetSum
        self.found = False
        self.dfs(root)
        return self.found
        