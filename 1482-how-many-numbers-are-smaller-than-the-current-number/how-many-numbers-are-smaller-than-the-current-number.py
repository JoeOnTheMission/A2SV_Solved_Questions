class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        d = {}
        for i,num in enumerate(s):
            if num not in d:
                d[num] = i
        res = []
        for num in nums:
            res.append(d[num])
        return res