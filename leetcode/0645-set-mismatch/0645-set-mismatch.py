class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0,0]
        x = set(nums)
        print(x)
        for i in range(len(nums)):
            if i != 0 and nums[i-1] == nums[i]:
                res[0] = nums[i]
    
            if i + 1 not in x:
                res[1] = i + 1
        return res