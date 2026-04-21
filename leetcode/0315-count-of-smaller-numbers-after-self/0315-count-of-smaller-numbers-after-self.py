class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        arr = [[i,num] for i,num in enumerate(nums)]
        def merge(arr1,arr2):
            i = 0 #for arr1
            j = 0 #for arr2
            sorted_arr = []
            while  i < len(arr1) and j < len(arr2):
            
                if arr1[i][1] <= arr2[j][1]:
                    sorted_arr.append(arr1[i])
                    res[arr1[i][0]] += j #update our output
                    i += 1
                else:
                    sorted_arr.append(arr2[j])
                    j += 1
            
            while i < len(arr1):#have left over right ones to update
                sorted_arr.append(arr1[i])
                res[arr1[i][0]] += len(arr2)
                i += 1
            sorted_arr.extend(arr1[i:])
            sorted_arr.extend(arr2[j:])
            return sorted_arr

        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])
            
            return merge(left, right)
        mergesort(arr)
        return res