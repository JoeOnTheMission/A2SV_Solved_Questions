class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running = 0
        min_running = nums[0]
        for i in range(len(nums)):
            running += nums[i]
            min_running = min(min_running,running)
        return ((min_running)*(-1)) + 1 if min_running < 0 else 1
        