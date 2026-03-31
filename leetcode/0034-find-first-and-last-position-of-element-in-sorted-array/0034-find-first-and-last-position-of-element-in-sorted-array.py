class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        found = False
        lower_bound = len(nums)
        upper_bound = len(nums)
        while low <= high:
            mid = (low + high) // 2
            #print(nums[mid],lower_bound)
            if nums[mid] >= target:
                lower_bound = mid
                high = mid - 1
            else:
                low = mid + 1
        #print(lower_bound)
        low = lower_bound
        high = len(nums) - 1
        while low <= high:
            mid = (low + high)//2
            #print(nums[mid],upper_bound)
            if nums[mid] > target:
                
                high = mid - 1
            else:
                upper_bound = mid
                low = mid + 1  
        #print(upper_bound)
        if lower_bound != len(nums) and upper_bound != len(nums):
            return [lower_bound,upper_bound]
      
       
        return [-1,-1]     