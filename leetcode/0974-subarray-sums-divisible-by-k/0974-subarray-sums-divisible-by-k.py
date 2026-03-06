class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
                
        #build prefix
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        seen = defaultdict(int)
        seen[0] += 1 
        res = 0
        for i in range(len(nums)):
            if nums[i] % k in seen:
                res += seen[nums[i]%k]
            seen[nums[i] % k] += 1
        return res