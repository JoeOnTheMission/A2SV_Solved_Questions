class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward_pre = [1,nums[0]]
        for i in range(1,len(nums)):
            forward_pre.append(forward_pre[-1] * nums[i])
        forward_pre.append(1)
       


        backward_pre = [1,nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            backward_pre.append(backward_pre[-1]*nums[i])
        backward_pre.append(1)
        backward_pre.reverse()
       
        res = []
        for i in range(len(nums)):
            res.append(forward_pre[i]*backward_pre[i+2])
        return res