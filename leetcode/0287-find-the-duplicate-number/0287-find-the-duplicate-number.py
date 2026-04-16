class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        n = len(nums)
        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                break
        fast = 0
        while True:
            fast = nums[fast]
            slow = nums[slow]
            if fast == slow:
                return fast
            