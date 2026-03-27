# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder_map = {val:i for i,val in enumerate(postorder)}
       
        def helper(left1,right1,left2,right2):#1 for pre and 2 for post
            if left1 > right1 or left2 > right2:
                return 
            root = TreeNode(preorder[left1])
            
            if left1 != right1:# has a subtree
                mid = postorder_map[preorder[left1+1]]

                left_size = mid - left2 + 1

                root.left = helper(left1 + 1, left1 + left_size, left2, mid)
                root.right = helper(left1 + left_size + 1, right1, mid + 1, right2 - 1)
            return root
           
            
        return helper(0, len(preorder)-1, 0,len(preorder)-1)


        