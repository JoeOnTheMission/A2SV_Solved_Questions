class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #clean up
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:# i don't care
                nums[i] = n+1
        #print(nums)
        for i in range(n):

            now = nums[i]
            if now < 0:
                index = (-1*now) - 1
            else:
                index = now - 1

            if index == n:
                continue
            else: 
                
                #mark
                if nums[index] < 0:#already marked
                    continue
                else:
                    nums[index] *= -1
        #finally
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        else:
            return i + 2