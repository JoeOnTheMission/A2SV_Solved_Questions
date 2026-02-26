class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0 
        window = 0
        tolerance = 1
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                tolerance -= 1
                while tolerance < 0:
                    if nums[left] == 0:
                        tolerance += 1
                    window -= nums[left]
                    left += 1
            else:        
                window += nums[right]
            res = max(res,right - left)
        return res