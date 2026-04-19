class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        
        for i in range(len(nums1)):
            target = nums1[i]
            left = i
            right = len(nums2) - 1
            best = i - 1  
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums2[mid] >= target:
                    best = mid     
                    left = mid + 1  
                else:
                    right = mid - 1
            
            if best >= i:
                res = max(res, best - i)
        
        return res