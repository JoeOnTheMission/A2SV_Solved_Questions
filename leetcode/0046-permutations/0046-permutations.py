class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def back(start,comb):
            if len(comb) == n:
                res.append(comb[:])
                return
            for i in range(0,n):
                if nums[i] not in comb:
                    comb.append(nums[i])
                    back(i+1,comb)
                    comb.pop()
        back(1,[])
        return res