class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def back(comb):
            if len(comb) == n:
                res.append(comb[:])
                return
            for i in range(0,n):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    back(comb)
                    comb.pop()
        back([])
        return res