class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = dict()
        stack = []
        for i in range(len(nums2)-1,-1,-1):
            if not stack:#empty stack
                ans[nums2[i]] = -1
            else:
                while stack and nums2[i] >= stack[-1]:
                    stack.pop()
                if stack:
                    ans[nums2[i]] = stack[-1]
                else:
                    ans[nums2[i]] = -1

            stack.append(nums2[i])
    
        res = []
        for num in nums1:
            res.append(ans[num])
        return res