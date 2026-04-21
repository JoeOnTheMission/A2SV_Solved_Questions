class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            #print(i , nums)
            correct = nums[i] - 1
            if nums[i] == nums[correct]:
                i += 1
            else:
                nums[i],nums[correct] = nums[correct],nums[i]
        res = []
        for i,num in enumerate(nums):
            #print(i+1,num)
            if num != i + 1:
                res.append(num)
        return res