# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,cur1,cur2):
        #print(cur1.val,cur2.val,self.res)
        if not self.res:# false found
            return 
        if not cur1 and not cur2:
            return
        elif not cur1 or not cur2:
            self.res = False
            #print("1")
            return 
        
        #check now
        if cur1.val != cur2.val:
            #print("2")
            self.res = False
            return 

        # check left
        if cur1.left and cur2.left:
            self.dfs(cur1.left,cur2.left)
        elif not cur1.left and not cur2.left:
            pass
        else:
            #print("3")
            self.res = False
            return
        #check right
        if cur1.right and cur2.right:
            self.dfs(cur1.right,cur2.right)
        elif not cur1.right and not cur2.right:
            pass
        else:
            #print("4")
            self.res = False
            return
            
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        self.dfs(p,q)
        return self.res
        