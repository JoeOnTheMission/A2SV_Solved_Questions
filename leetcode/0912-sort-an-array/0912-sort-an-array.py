class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1,arr2):
            i,j = 0,0
            res = []
            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1
            res.extend(arr1[i:])
            res.extend(arr2[j:])
            
            return res
        
        def recursive(left,right,arr):
            if left == right:
                return [nums[left]] 
            mid = left + (right-left)//2
            left_arr = recursive(left,mid,arr)
            right_arr = recursive(mid+1,right,arr)
            return merge(left_arr,right_arr)
        return recursive(0,len(nums)-1,nums)