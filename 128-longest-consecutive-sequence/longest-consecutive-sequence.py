class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        i = 0
        res = 1
        length = 0
        if len(nums) == 0:
            return 0

        while i + 1 < len(nums):
            
            if nums[i] + 1 == nums[i+1]:
                
                length = 0
                while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                    
                    length += 1
                    i += 1
                    
                res = max(res,length + 1)
            
            i += 1
        
        return res