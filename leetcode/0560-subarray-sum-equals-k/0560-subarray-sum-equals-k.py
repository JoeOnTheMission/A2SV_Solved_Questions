class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] += 1

        running = 0
        res = 0
        
        for i in range(len(nums)):
            running += nums[i]
            needed = running - k
            
            if needed in seen:
                res += seen[needed]
            seen[running] += 1
        return res