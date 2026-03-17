class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        left_min = [] 
        minimum = nums[0]
        for i in range(len(nums)):
            minimum = min(minimum,nums[i])
            left_min.append(minimum)
        stack = []

        for i in range(len(nums)-1,0,-1):
            if nums[i] != left_min[i]:
                while stack and stack[-1] <= left_min[i]:
                    stack.pop()
                if stack and stack[-1] < nums[i]:
                    return True 
                stack.append(nums[i])
        return False