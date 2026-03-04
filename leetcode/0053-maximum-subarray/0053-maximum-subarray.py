class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      

        min_runnning = 0
        running = 0
        res = nums[0]
        for i in range(len(nums)):
            running += nums[i]
            res = max(res,running - min_runnning)
            min_runnning = min(min_runnning,running)

        return res