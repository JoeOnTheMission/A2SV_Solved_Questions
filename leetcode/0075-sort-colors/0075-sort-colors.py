class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def partition(l,r):
            pivot = nums[l]
            write = l + 1

            for read in range(l+1,r+1):
                if nums[read] < pivot:
                    nums[read],nums[write] = nums[write],nums[read]
                    write += 1
            nums[write-1],nums[l] = nums[l],nums[write-1]
            return write - 1

            
        def quicksort(left,right):
            if left >= right:
                return 
            pivot_index = partition(left,right)
            quicksort(left,pivot_index - 1)
            quicksort(pivot_index + 1,right)    

        quicksort(0,len(nums)-1)