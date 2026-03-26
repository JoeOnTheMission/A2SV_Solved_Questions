class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def back(start,comb):
            #print(start,comb)
            res.append(comb[:])
            for i in range(start,n):
                comb.append(nums[i])
                back(i+1,comb)
                comb.pop()
        back(0,[])
        return res