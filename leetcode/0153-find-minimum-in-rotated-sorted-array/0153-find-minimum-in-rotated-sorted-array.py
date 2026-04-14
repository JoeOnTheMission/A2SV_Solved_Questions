class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        if nums[0] < nums[-1]:
            #already sorted
            return nums[0]

        n = len(nums)
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left + right)//2
            print(left,mid,right)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid 
            print(left,right)

        return nums[right] 