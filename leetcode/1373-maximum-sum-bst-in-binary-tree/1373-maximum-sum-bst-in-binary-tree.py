# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node):
            #print(node.val,self.res)
            if not node:
                return []
            left = []
            right = []
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            
            good_left = False
            good_right = False
            now = node.val
            if left != False:
                if len(left) == 0:
                    good_left = True
                elif left[-1] < now:
                    good_left = True

            if right != False:
                if len(right) == 0:
                    good_right = True
                elif right[0] > now:
                    good_right = True

            if good_left and good_right:
                now_arr = []
                now_arr.extend(left)
                now_arr.append(now)
                now_arr.extend(right)
                self.res = max(self.res,sum(now_arr))
                return now_arr
            return False
        dfs(root)
        return self.res
            