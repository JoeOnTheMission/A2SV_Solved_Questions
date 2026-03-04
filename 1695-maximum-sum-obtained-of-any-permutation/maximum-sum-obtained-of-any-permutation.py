class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre = [0]*(len(nums)+1)
        for l,r in requests:
            pre[l] += 1
            pre[r+1] -= 1
        for i in range(1,len(nums)):
            pre[i] += pre[i-1]
        pre.sort(reverse=True)
        nums.sort(reverse=True)
        res = 0
        for i in range(len(nums)):
            res += nums[i]*pre[i]
        return res % ((10**9) + 7)