class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
                
        left = 0
        res = 0
        window = defaultdict(int)

        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) > k:
                window[nums[left]] -= 1   
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            res += right - left + 1
  

        left = 0
        res2 = 0
        window = defaultdict(int)

        for right in range(len(nums)):
            window[nums[right]] += 1
            while len(window) >= k:
                window[nums[left]] -= 1   
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1
            res2 += right - left + 1
    
        return res - res2