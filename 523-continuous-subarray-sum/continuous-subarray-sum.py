class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        seen = {0: -1}  # remainder -> first index

        for i, num in enumerate(nums):
            prefix += num
            remainder = prefix % k
            
            if remainder in seen:
                if i - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = i
                
        return False