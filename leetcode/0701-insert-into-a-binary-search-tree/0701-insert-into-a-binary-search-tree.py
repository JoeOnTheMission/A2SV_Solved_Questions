# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        new = TreeNode(val)
        done = False
        if not root:
            root = new
            done = True
        while not done:
             
            if cur.val > val:#go to the left
                if cur.left:
                    cur = cur.left
                else:
                    #reached add point
                    cur.left = new
                    done = True
            if cur.val < val:#go to the right
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = new
                    done = True
        return root

            
