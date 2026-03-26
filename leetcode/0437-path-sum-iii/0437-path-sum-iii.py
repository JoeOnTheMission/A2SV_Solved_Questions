# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,cur):
        if not cur:
            return

        self.pre += cur.val
        
        if self.pre - self.target in self.have:
            self.res += self.have[self.pre-self.target]
        self.have[self.pre] += 1

        if cur.right:
            self.dfs(cur.right)
            self.have[self.pre] -= 1
            if self.have[self.pre] == 0:
                self.have.pop(self.pre)
            self.pre -= cur.right.val


        if cur.left:
            self.dfs(cur.left)
            self.have[self.pre] -= 1
            if self.have[self.pre] == 0:
                self.have.pop(self.pre)
            self.pre -= cur.left.val
        

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.have = defaultdict(int)
        self.have[0] += 1
        self.pre = 0
        self.target  = targetSum
        self.res = 0
        self.dfs(root)
        return self.res
