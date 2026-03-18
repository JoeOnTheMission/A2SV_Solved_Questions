class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        prev = nums[-1]
        op = 0
        for i in range(len(nums)-2,-1,-1):
            now = nums[i]
            if now > prev:
                k = (now + prev - 1) // prev  
                op += k - 1
                prev = now // k
            else:
                prev = now
        return op
