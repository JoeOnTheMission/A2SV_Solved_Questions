class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i = 0 
        j = len(height) - 1
        while i < j:
            current_capacity = (j - i) * min(height[i],height[j])
            res = max(res,current_capacity)
            if height[i] < height[j]:# it is better to push left pointer
                i += 1
            else:
                j -= 1
        return res
            