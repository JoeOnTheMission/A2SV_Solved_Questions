class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        seen = defaultdict(int)
        seen[0] += 1
        running = 0
        res = 0
        for i in range(len(nums)):
            running += nums[i]
            needed = running - goal
    
            if needed in seen:
                res+= seen[needed]
            seen[running] += 1
            
        return res