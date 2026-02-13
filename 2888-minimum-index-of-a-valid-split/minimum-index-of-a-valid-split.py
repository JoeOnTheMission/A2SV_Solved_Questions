class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        nums_count =  Counter(nums)
        dominant,dominant_count = nums_count.most_common(1)[0][0], nums_count.most_common(1)[0][1]
        left = 0

        for i in range((len(nums)-1)):
            num = nums[i]
            if nums[i] == dominant:
                left += 1
    
            #valid 
            if left * 2 > i+1 and (dominant_count - left) * 2 > (len(nums)- i -1):
                return i
                break
        else:
            return -1
            