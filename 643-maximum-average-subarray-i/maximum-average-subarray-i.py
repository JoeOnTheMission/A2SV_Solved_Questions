class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #build window
        window_sum = 0

        for i in range(k):
            window_sum += nums[i] 
        res = window_sum/k
        #move the window 
        for j in range(len(nums)-k):
            first = nums[j]
            last = nums[j+k]
            window_sum -= first
            window_sum += last
            res = max(res,window_sum/k)
        return res
