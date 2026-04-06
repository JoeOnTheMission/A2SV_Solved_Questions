# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(cur):
            if not cur:
                return [0,0]
            left_size, left_coin = dfs(cur.left)
            right_size, right_coin = dfs(cur.right)

            size = 1 + left_size + right_size
            coin = cur.val + left_coin + right_coin
            self.res += abs(coin - size)
            return [size,coin]
        dfs(root)
        return self.res