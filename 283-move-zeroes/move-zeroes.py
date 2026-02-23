class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        done = False
        holder = 0
        while not done:

            for seeker in range(holder,len(nums)):
                if nums[seeker] != 0:
                    nums[seeker],nums[holder] = nums[holder], nums[seeker]
                    holder += 1
                    continue
            else:
                done = True
