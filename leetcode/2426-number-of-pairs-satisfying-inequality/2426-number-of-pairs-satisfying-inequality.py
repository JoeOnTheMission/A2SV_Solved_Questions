class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        self.res = 0
        arr = [nums1[k] - nums2[k] for k in range(len(nums1))]

        def mergesort(left,right):
            if left == right:
                return [arr[left]]

            mid = left + (right - left)//2
            left = mergesort(left,mid)
            right = mergesort(mid+1,right)

            #update our res
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                self.res += len(right) - j
            #merge left and right
            merged = []
            i = 0
            j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            merged.extend(left[i:])
            merged.extend(right[j:])

            return merged
        mergesort(0,len(arr)-1)
        return self.res