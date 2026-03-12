class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return True

        can = [0]*len(nums)
        for i,num in enumerate(nums):
            if i + 1 < len(can): 
                can[i+1] += 1
            if i + 1 + num < len(can):
                can[i+1+num] -= 1

        for i in range(1,len(nums)):
            can[i] += can[i-1]
            
        #print(can)
        for i in range(1,len(nums)):
            if can[i] == 0:
                return False
        return True
            
            