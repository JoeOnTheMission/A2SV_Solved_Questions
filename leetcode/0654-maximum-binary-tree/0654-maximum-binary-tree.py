# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def backtrack(start,end):
            print(start,end)
            if start > end:
                return None
            max_index = start
            for i in range(start, end + 1):
                if nums[i] > nums[max_index]:
                    max_index = i
            max_value = nums[max_index]

            left = backtrack(start,max_index-1)
            right = backtrack(max_index+1,end)
            node = TreeNode(max_value,left,right)
            return node
        return backtrack(0,len(nums)-1)
        