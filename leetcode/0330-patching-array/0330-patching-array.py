class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i = 0
        res = 0
        now_sum = 1
        while now_sum <= n:
            if i < len(nums) and nums[i] <= now_sum:
                now_sum += nums[i]
                i += 1
            else:
                now_sum *= 2
                res += 1
        return res 