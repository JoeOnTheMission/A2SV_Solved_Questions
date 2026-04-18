class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.res = 0

        def merge_sort(l, r):
            if l == r:
                return [arr[l]]

            mid = (l + r) // 2
            left = merge_sort(l, mid)
            right = merge_sort(mid + 1, r)

           
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                self.res += len(right) - j

          
            merged = []
            i = j = 0

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

        merge_sort(0, len(arr) - 1)
        return self.res