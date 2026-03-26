# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,cur):
        #print(self.path,self.cur_sum,self.target)
        if not cur:
            return
        if cur.left:
            self.cur_sum += cur.left.val
            self.path.append(cur.left.val)
            self.dfs(cur.left)
            self.cur_sum -= cur.left.val
            self.path.pop()
        if cur.right:
            self.cur_sum += cur.right.val
            self.path.append(cur.right.val)
            self.dfs(cur.right)
            self.cur_sum -= cur.right.val
            self.path.pop()
        if not cur.left and not cur.right:#leaf node
            if self.cur_sum == self.target:
                self.res.append(self.path[:])#remember to append the copy not the pointer to the same array multiple times

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.res = []
        self.path = [root.val]
        self.cur_sum = root.val
        self.target = targetSum
        self.dfs(root)
        return self.res